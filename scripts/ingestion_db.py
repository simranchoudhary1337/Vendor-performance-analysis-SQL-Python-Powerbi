{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "36169644-20c4-479b-9c05-115722a13840",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import os\n",
    "from sqlalchemy import create_engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ad9afc6e-264c-4d4e-a24e-4cdaa112fce9",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine('sqlite:///inventory.db')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "15910cba-9467-4e5e-aee9-4594b1ebae18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(206529, 9)\n",
      "(224489, 9)\n",
      "(2372474, 16)\n",
      "(12261, 9)\n",
      "(5543, 10)\n"
     ]
    }
   ],
   "source": [
    "for file in os.listdir('data'):\n",
    "    if '.csv' in file:\n",
    "        df=pd.read_csv('data/'+file)\n",
    "        print(df.shape)\n",
    "        ingest_db(df, file[:-4], engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "838e2288-a223-410d-8e64-0f5137288dd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#when data is coming cont. from server and want to store it in db so scripting\n",
    "\n",
    "def ingest_db(df, table_name, engine):\n",
    "    df.to_sql(table_name, con=engine , if_exists='replace', index=False )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "94a98c56-89ea-4945-8ff2-7791843f5c25",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ingest_single_file(file_path, table_name, engine, chunksize=100000): \n",
    "    for chunk in pd.read_csv(file_path, chunksize=chunksize):\n",
    "       chunk.to_sql(table_name, con=engine, if_exists=\"append\", index=False) \n",
    "        \n",
    "ingest_single_file(\"data/sales.csv\", \"sales\", engine)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb548f03-a416-41f5-9f6e-93756d03fa55",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
