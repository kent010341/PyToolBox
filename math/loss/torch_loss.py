from . import loss
import torch

def MSE(real, predict):
    return loss.MSE(real, predict)

def RMSE(real, predict):
    return loss.RMSE(real, predict)

def MAE(real, predict, lib):
    return loss.MAE(real, predict, torch)

def MAPE(real, predict, lib):
    return loss.MAPE(real, predict, torch)

def SNR(real, predict, lib):
    return loss.SNR(real, predict, torch)

def SSIM(real, predict, c1=1e-4, c2=3e-4):
    return loss.SSIM(real, predict, c1=c1, c2=c2)
