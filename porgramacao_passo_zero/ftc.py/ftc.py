{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a8f4f81-9bd3-4084-8551-56da8fdf22d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "usuarios = {\n",
    "\"nome\" : [\"Meigarom\", \"Claudio\", \"Fernando\", \"Diego\", \"André\"],\n",
    "\"idade\" : [34, 30, 36, 25, 36],\n",
    "\"cidade\" : [\"Indaiatuba\", \"Arcos\", \"Ouro Fino\", \"Itapira\", \"Curitiba\"],\n",
    "\"estado\": [\"SP\", \"RJ\", \"SP\", \"RJ\", \"RJ\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame ( usuarios )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "45c65130-14e0-43fa-b357-b171558319d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /Users/fernanda/anaconda3/lib/python3.10/site-packages (1.5.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2022.7)\n",
      "Requirement already satisfied: numpy>=1.21.0 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (1.23.5)\n",
      "Requirement already satisfied: six>=1.5 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "62956743-f51a-4d38-819a-31fa352cea0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "usuarios = {\n",
    "\"nome\" : [\"Meigarom\", \"Claudio\", \"Fernando\", \"Diego\", \"André\"],\n",
    "\"idade\" : [34, 30, 36, 25, 36],\n",
    "\"cidade\" : [\"Indaiatuba\", \"Arcos\", \"Ouro Fino\", \"Itapira\", \"Curitiba\"],\n",
    "\"estado\": [\"SP\", \"RJ\", \"SP\", \"RJ\", \"RJ\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame ( usuarios )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "283edeff-1c76-4202-bfe4-6f9c6df4c128",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1213601677.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[17], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    sudo pacman -S  python-pandas\u001b[0m\n\u001b[0m         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "sudo pacman -S  python-pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4eff6018-a830-446c-8e59-dc9561e39977",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /Users/fernanda/anaconda3/lib/python3.10/site-packages (1.5.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2022.7)\n",
      "Requirement already satisfied: numpy>=1.21.0 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (1.23.5)\n",
      "Requirement already satisfied: six>=1.5 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f51e1387-f85c-4851-b61e-32b3c37d5858",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       nome  idade      cidade estado\n",
      "0  Meigarom     34  Indaiatuba     SP\n",
      "1   Claudio     30       Arcos     RJ\n",
      "2  Fernando     36   Ouro Fino     SP\n",
      "3     Diego     25     Itapira     RJ\n",
      "4     André     36    Curitiba     RJ\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "usuarios = {\n",
    "\"nome\" : [\"Meigarom\", \"Claudio\", \"Fernando\", \"Diego\", \"André\"],\n",
    "\"idade\" : [34, 30, 36, 25, 36],\n",
    "\"cidade\" : [\"Indaiatuba\", \"Arcos\", \"Ouro Fino\", \"Itapira\", \"Curitiba\"],\n",
    "\"estado\": [\"SP\", \"RJ\", \"SP\", \"RJ\", \"RJ\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame ( usuarios )\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "de270d75-15c5-4936-a181-ebaf4383326e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame()\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "535d8df6-91c8-4409-9537-4f433878ed11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>estado</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Meigarom</td>\n",
       "      <td>34</td>\n",
       "      <td>Indaiatuba</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claudio</td>\n",
       "      <td>30</td>\n",
       "      <td>Arcos</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Fernando</td>\n",
       "      <td>36</td>\n",
       "      <td>Ouro Fino</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Diego</td>\n",
       "      <td>25</td>\n",
       "      <td>Itapira</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>André</td>\n",
       "      <td>36</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       nome  idade      cidade estado\n",
       "0  Meigarom     34  Indaiatuba     SP\n",
       "1   Claudio     30       Arcos     RJ\n",
       "2  Fernando     36   Ouro Fino     SP\n",
       "3     Diego     25     Itapira     RJ\n",
       "4     André     36    Curitiba     RJ"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "usuarios = {\n",
    "\"nome\" : [\"Meigarom\", \"Claudio\", \"Fernando\", \"Diego\", \"André\"],\n",
    "\"idade\" : [34, 30, 36, 25, 36],\n",
    "\"cidade\" : [\"Indaiatuba\", \"Arcos\", \"Ouro Fino\", \"Itapira\", \"Curitiba\"],\n",
    "\"estado\": [\"SP\", \"RJ\", \"SP\", \"RJ\", \"RJ\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame ( usuarios )\n",
    "(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b22bca69-456b-4684-be6d-0160cc9e93ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nome</th>\n",
       "      <th>idade</th>\n",
       "      <th>cidade</th>\n",
       "      <th>estado</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Meigarom</td>\n",
       "      <td>34</td>\n",
       "      <td>Indaiatuba</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claudio</td>\n",
       "      <td>30</td>\n",
       "      <td>Arcos</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Fernando</td>\n",
       "      <td>36</td>\n",
       "      <td>Ouro Fino</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Diego</td>\n",
       "      <td>25</td>\n",
       "      <td>Itapira</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>André</td>\n",
       "      <td>36</td>\n",
       "      <td>Curitiba</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       nome  idade      cidade estado\n",
       "0  Meigarom     34  Indaiatuba     SP\n",
       "1   Claudio     30       Arcos     RJ\n",
       "2  Fernando     36   Ouro Fino     SP\n",
       "3     Diego     25     Itapira     RJ\n",
       "4     André     36    Curitiba     RJ"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "usuarios = {\n",
    "\"nome\" : [\"Meigarom\", \"Claudio\", \"Fernando\", \"Diego\", \"André\"],\n",
    "\"idade\" : [34, 30, 36, 25, 36],\n",
    "\"cidade\" : [\"Indaiatuba\", \"Arcos\", \"Ouro Fino\", \"Itapira\", \"Curitiba\"],\n",
    "\"estado\": [\"SP\", \"RJ\", \"SP\", \"RJ\", \"RJ\"]\n",
    "}\n",
    "df = pd.DataFrame ( usuarios )\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "5af7bc97-3d05-463d-9af4-53e82b940157",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   idade estado      cidade\n",
      "0     34     SP  Indaiatuba\n",
      "1     30     RJ       Arcos\n",
      "2     36     SP   Ouro Fino\n",
      "3     25     RJ     Itapira\n"
     ]
    }
   ],
   "source": [
    "colunas = [\"idade\", \"estado\", \"cidade\"]\n",
    "df_selecionados = df.loc[0:3, colunas]\n",
    "print(df_selecionados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "ff7fb945-a443-4051-b1ee-c39f03a7fbee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /Users/fernanda/anaconda3/lib/python3.10/site-packages (1.5.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (2022.7)\n",
      "Requirement already satisfied: numpy>=1.21.0 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from pandas) (1.23.5)\n",
      "Requirement already satisfied: six>=1.5 in /Users/fernanda/anaconda3/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "dca7e504-f041-45b1-88a5-05bfc259dffd",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'google'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[50], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m \n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mio\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgoogle\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m colab \u001b[38;5;28;01mas\u001b[39;00m cl \n\u001b[1;32m      4\u001b[0m file_upload \u001b[38;5;241m=\u001b[39m cl\u001b[38;5;241m.\u001b[39mfiles\u001b[38;5;241m.\u001b[39mupload()\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'google'"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import io\n",
    "from google import colab as cl \n",
    "file_upload = cl.files.upload()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27a1f60a-0a3a-4d33-a34f-e5c6a9446368",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f2c902fa-15e9-4e06-85b4-93e1da7cc09d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'google'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[50], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m \n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mio\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgoogle\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m colab \u001b[38;5;28;01mas\u001b[39;00m cl \n\u001b[1;32m      4\u001b[0m file_upload \u001b[38;5;241m=\u001b[39m cl\u001b[38;5;241m.\u001b[39mfiles\u001b[38;5;241m.\u001b[39mupload()\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'google'"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import io\n",
    "from google import colab as cl \n",
    "file_upload = cl.files.upload()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "760688c3-6e59-4a77-a40f-2f1b138e3880",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
