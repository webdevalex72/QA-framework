# config/utils.py
"""This module define function to get actual path to root project"""
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent
