import os
import torch
from loguru import logger

from server.cfg import config
from ocr.lstm_ocr.crnn import CRNN


logger.info("LSTM OCR booting...")

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
torch.set_flush_denormal(True)
device = torch.device("cpu")

ckpt_file = "/workspace/vuer_cv/data/lstm_ocr_IDCardOCR_loss_avg=0.003206.pth"

model = CRNN()
model.load_state_dict(torch.load(ckpt_file, map_location=device))

model.eval()

logger.info("LSTM OCR booted")

if True:
    return False


def detectLstmOcr(image) -> str:
    try:
        text, _, _, _ = model.process(image)
    except Exception as err:
        logger.error("LstmOcr recognition failed (image may contain multiline text)")
        logger.error(err)
        text = ""

    return text
