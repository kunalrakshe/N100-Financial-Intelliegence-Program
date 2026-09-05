{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "19345afa-b681-4810-a4f7-e3a89fc70c6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "def normalize_year(value):\n",
    "    if pd.isna(value):\n",
    "        return None\n",
    "\n",
    "    value = str(value).strip()\n",
    "\n",
    "    match = re.search(r\"(20\\d{2})\", value)\n",
    "\n",
    "    if match:\n",
    "        return int(match.group(1))\n",
    "\n",
    "    return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f5dae70b-746e-40d1-aa9a-2a788d0c588c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024\n",
      "2024\n",
      "2024\n"
     ]
    }
   ],
   "source": [
    "print(normalize_year(\"FY2024\"))\n",
    "print(normalize_year(\"2024-25\"))\n",
    "print(normalize_year(2024))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "85642380-37c2-476f-8832-208c90c9dab9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def normalize_ticker(value):\n",
    "    if pd.isna(value):\n",
    "        return None\n",
    "\n",
    "    value = str(value).strip().upper()\n",
    "\n",
    "    value = value.replace(\"NSE:\", \"\")\n",
    "    value = value.replace(\"BSE:\", \"\")\n",
    "\n",
    "    return value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3eb3467e-bdff-4090-86d5-86dafa67e4de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RELIANCE\n",
      "RELIANCE\n"
     ]
    }
   ],
   "source": [
    "print(normalize_ticker(\" reliance \"))\n",
    "print(normalize_ticker(\"NSE:RELIANCE\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
