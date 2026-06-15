{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "bcd33f5a-3a0f-4b03-b2a5-cd29cb711362",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def convert_col_to_float(col, custom_na=None, missing_value=np.nan):\n",
    "    try:\n",
    "        new_col = col.astype(np.float64)\n",
    "        return new_col\n",
    "    except:\n",
    "        new_col = []\n",
    "        common_na_str = { '', ' ', '\\t', 'na', 'nan', 'NA', 'Na', 'NaN', '?', '-' }\n",
    "        if custom_na is not None and type(custom_na) == str:\n",
    "            common_na_str.add(custom_na)\n",
    "        elif custom_na is not None and (type(custom_na) == list or type(custom_na) == set or type(custom_na) == tuple):\n",
    "            for na in custom_na:\n",
    "                common_na_str.add(na)\n",
    "        elif custom_na is not None:\n",
    "            common_na_str.add(str(custom_na))\n",
    "        na_pos = []\n",
    "        float_pos = []\n",
    "        for i in range(len(col)):\n",
    "            if col[i].strip() in common_na_str:\n",
    "                na_pos.append(i)\n",
    "                new_col.append(missing_value)\n",
    "            else:\n",
    "                try:\n",
    "                    new_col.append(float(col[i].strip()))\n",
    "                    float_pos.append(i)\n",
    "                except:\n",
    "                    return col.copy()\n",
    "        return new_col\n",
    "                    \n",
    "\n",
    "def load_csv(filepath, delimiter=',', missing_value=np.nan, custom_na=None, skip_header=True):\n",
    "    data = np.loadtxt(\n",
    "        filepath, \n",
    "        delimiter=delimiter,\n",
    "        dtype=str, \n",
    "        skiprows=1 if skip_header else 0\n",
    "    )\n",
    "    try:\n",
    "        data = data.astype(np.float64)\n",
    "    except:\n",
    "        new_data = []\n",
    "        for col_index in range(data.shape[1]):\n",
    "            new_data.append(convert_col_to_float(data[:, col_index], \n",
    "                                                 missing_value=missing_value, \n",
    "                                                 custom_na=custom_na))\n",
    "        new_data = np.array(new_data).T\n",
    "        try: \n",
    "            data = new_data.astype(np.float64)\n",
    "        except:\n",
    "            pass\n",
    "    return data\n",
    "\n",
    "def save_csv(filepath, data, delimiter=',', columns=[]):\n",
    "    if data.dtype == np.int32 or data.dtype == np.int64:\n",
    "        fmt = '%d'\n",
    "    elif data.dtype == np.float64:\n",
    "        fmt = '%.5f'\n",
    "    else:\n",
    "        fmt = '%.18e'\n",
    "    np.savetxt(\n",
    "        filepath, \n",
    "        data, \n",
    "        fmt=fmt, \n",
    "        delimiter=delimiter,  \n",
    "        header=delimiter.join(columns) if columns is not None and len(columns) else '',\n",
    "        comments=''\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "a0f6e3ce-22e8-4159-98b2-6149f9b6b066",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.,  2.,  3.],\n",
       "       [ 2., nan,  4.],\n",
       "       [ 2.,  3.,  4.]])"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_csv(\"data_comma.txt\", delimiter=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "e2af00a3-6c5c-457b-a83f-06e6ecdd379e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['A', 'B', 'C', 'D'],\n",
       "       ['1', '2', '3', 'M'],\n",
       "       ['2', ' ? ', '4', 'M'],\n",
       "       ['2', '3', '4', 'F']], dtype='<U3')"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_csv(\"data_comma-Copy1.txt\", delimiter=',', skip_header=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "809a4339-9a58-4976-bd47-0dc89d0aece7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.,  2., nan],\n",
       "       [ 4.,  5.,  6.],\n",
       "       [nan,  2.,  3.],\n",
       "       [nan,  1.,  2.],\n",
       "       [nan,  2., nan]])"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_csv(\"data_space.txt\", delimiter=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "936b31b4-b6eb-4973-8204-c942a13fdf51",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = load_csv(\"data_space.txt\", delimiter=' ')\n",
    "save_csv(\"data_1_out.csv\", data, delimiter=',', columns=[\"id\", \"sfda\", \"sadfs\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e76d985a-4f8e-4882-bb67-feb086217e60",
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
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
