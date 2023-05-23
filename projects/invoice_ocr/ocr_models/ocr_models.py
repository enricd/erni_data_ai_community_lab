import easyocr
import cv2
import numpy as np
import pytesseract
import os
from transformers import DonutProcessor, VisionEncoderDecoderModel
import torch
import re
import pprint
#pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def easyOCR_Image2Text(image):

    ## Y tolerance to format the text in different lines
    Tolerance = 30

    reader = easyocr.Reader(['es', 'en'])
    result = reader.readtext(image)

    ## Order the text from top left to bottom right
    result.sort(key=lambda x: ((x[0][0][1]+x[0][2][1])//Tolerance, (x[0][0][0]+x[0][2][0])/2))

    ## Extracting the per line and adding carry return
    resFormat = ""
    LastY = 0
    for r in result:
        text = r[1]
        YInitPos = r[0][0][1]
        if not ((LastY - Tolerance//2 < YInitPos) and (LastY + Tolerance//2 > YInitPos)):
            resFormat += "  \n"
        resFormat += text + " "
        LastY = YInitPos
    return resFormat


def pytesseract_Image2Text(image):

    text = pytesseract.image_to_string(image)
    return text


def donut_Image2Text(image):

    if(len(image.shape) <= 2):
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
    model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)



    # prepare decoder inputs
    task_prompt = "<s_cord-v2>"
    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids

    pixel_values = processor(image, return_tensors="pt").pixel_values

    outputs = model.generate(
        pixel_values.to(device),
        decoder_input_ids=decoder_input_ids.to(device),
        max_length=model.decoder.config.max_position_embeddings,
        early_stopping=True,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        num_beams=1,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
    )

    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
    sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()  # remove first task start token
    text = pprint.pformat(processor.token2json(sequence))
    return (text)
