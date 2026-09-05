{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eadfae03-1c36-4e7e-a6bf-b51caacb0468",
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
   "id": "11479cdb-92aa-4ab6-b182-a31422a695ab",
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
   "id": "29a703ec-ad59-4927-9d4e-e07f38e5fd47",
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
   "id": "79eab661-6dfb-40c9-ae19-b61c500a5105",
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
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c2385d55-8a8f-44cb-876d-09bb55264e47",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'normaliser'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m pandas \u001b[38;5;28;01mas\u001b[39;00m pd\n\u001b[32m      2\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m normaliser \u001b[38;5;28;01mimport\u001b[39;00m normalize_year, normalize_ticker\n\u001b[32m      4\u001b[39m \n\u001b[32m      5\u001b[39m \n\u001b[32m      6\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m load_excel():\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'normaliser'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "from normaliser import normalize_year, normalize_ticker\n",
    "\n",
    "\n",
    "def load_excel():\n",
    "    df = pd.read_excel(\"C:/N100 Finacial Intelligence Platform/data/companies.xlsx\")\n",
    "\n",
    "    df.columns = (\n",
    "        df.columns\n",
    "        .str.strip()\n",
    "        .str.lower()\n",
    "        .str.replace(\" \", \"_\", regex=False)\n",
    "    )\n",
    "\n",
    "    if \"year\" in df.columns:\n",
    "        df[\"year\"] = df[\"year\"].apply(normalize_year)\n",
    "\n",
    "    if \"ticker\" in df.columns:\n",
    "        df[\"ticker\"] = df[\"ticker\"].apply(normalize_ticker)\n",
    "\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f56a1b0-1743-426d-a702-2311459657b5",
   "metadata": {},
   "outputs": [],
   "source": []
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
