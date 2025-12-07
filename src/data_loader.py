"""
Refugee Migration Data Loader Module

This module provides object-oriented classes for loading and managing
refugee migration data from multiple sources including UNHCR, IDMC,
World Bank, and supplementary datasets.

Author: Your Name
Date: December 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Dict, List, Union
from abc import ABC, abstractmethod
import logging
from datetime import datetime
import requests
from io import StringIO