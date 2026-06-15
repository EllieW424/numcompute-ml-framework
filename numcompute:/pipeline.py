{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f3b5cadd-7bb3-459e-8baf-9b2ea13f7e0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])\n",
    "\n",
    "from preprocessing import *\n",
    "\n",
    "class Pipeline:\n",
    "\n",
    "    def __init__(self, steps):\n",
    "        self._steps = steps\n",
    "        self._named_steps = {\n",
    "            name: step for name, step in steps\n",
    "        }\n",
    "\n",
    "    def fit(self, X, y):\n",
    "        for step in self._steps:\n",
    "            name, func = step\n",
    "\n",
    "            if type(func) == StandardScaler:\n",
    "                X = func.fit(X)\n",
    "            # elif type(func) == XXXX:\n",
    "                # func.fit(X, y)\n",
    "        return self\n",
    "\n",
    "    def transform(self, X, y):\n",
    "        for step in self._steps:\n",
    "            name, func = step\n",
    "\n",
    "            if type(func) == StandardScaler:\n",
    "                X = func.transform(X)\n",
    "            # elif type(func) == XXXX:\n",
    "                # func.fit(X, y)\n",
    "        return X, y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4f94720e-d114-49be-9af1-b3c7a12fb496",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 2.],\n",
       "       [4., 5.],\n",
       "       [1., 2.],\n",
       "       [1., 1.],\n",
       "       [1., 2.]])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from io1 import load_csv, save_csv\n",
    "\n",
    "data = load_csv(\"data_space.txt\", delimiter=' ', missing_value=1.0)\n",
    "X, y = data[:, :-1], data[:, -1]\n",
    "\n",
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "06f52ce6-21b5-498d-9d9c-0a61fadda210",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 2.],\n",
       "       [4., 5.],\n",
       "       [1., 2.],\n",
       "       [1., 1.],\n",
       "       [1., 2.]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe = Pipeline([('scaler', StandardScaler)])\n",
    "X1, y1 = pipe.fit(X, y).transform(X, y)\n",
    "X1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "385cdfe4-dee0-4799-b128-7f14e89fd2ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "save_csv(\"data_1_out.csv\", data, delimiter=',', columns=[\"id\", \"sfda\", \"sadfs\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c4632da8-5cb2-4dd8-98cd-22837c7f0de7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a223545a-52d0-44cd-9c83-c8e571f4d1cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['Male', 1], ['Female', 3], ['Female', 2]]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "enc = OneHotEncoder(handle_unknown='ignore')\n",
    "X = [['Male', 1], ['Female', 3], ['Female', 2]]\n",
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "506aa482-2f39-46cc-bdc3-e57d1bcc2380",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 1., 0., 0.],\n",
       "       [0., 1., 0., 0., 1.]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "enc.fit(X)\n",
    "\n",
    "enc.transform([['Female', 1], ['Male', 3]]).toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "def8c326-ba4c-4cf4-98e1-1c12df3e8acd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['female', 'male'], dtype='<U6')"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "unique_values = np.unique([[\"female\", \"male\", \"male\"]])\n",
    "unique_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "790ebb7c-9913-4ff6-8477-4b6239110f07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{np.str_('female'): 0, np.str_('male'): 1}"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "{v: i for i, v in enumerate(unique_values)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "97806f35-3606-451e-9c77-dc7f5d355cd2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0.],\n",
       "       [0., 0.],\n",
       "       [0., 0.]])"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros((3, len(unique_values)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "54047e6b-31bd-4997-abbc-fda5fc493781",
   "metadata": {},
   "outputs": [],
   "source": [
    "n_rows = 3\n",
    "col_idx = 0\n",
    "_number = [2]\n",
    "_ids = [{'Female': 0, 'Male': 1}]\n",
    "unique_values = np.array(['Female', 'Male'])\n",
    "\n",
    "col = ['Female', 'Male', 'XXXXXX']\n",
    "\n",
    "col_tf = np.zeros((n_rows, _number[col_idx]))\n",
    "v_id = np.array([ _ids[col_idx].get(value, -1) for value in col ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "4e3c813b-db4e-4e34-8c8a-018b31cf3e39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1, -1])"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "1e357f66-51bc-4abd-bc3b-82f3d330eac2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0.],\n",
       "       [1., 0.],\n",
       "       [0., 1.]])"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "eye = np.concatenate((np.zeros((1,2)), np.eye(2)))\n",
    "eye"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9d7e25cc-8ec5-49b5-96ea-987c88afd6aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0.],\n",
       "       [0., 1.],\n",
       "       [0., 0.]])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encs = eye[v_id + 1]\n",
    "oh_encs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "12d2c728-572a-43c5-a354-bfc1b4594d9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 1., 0.],\n",
       "       [0., 0., 1.],\n",
       "       [0., 0., 0.]])"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encs = np.concatenate((np.zeros((oh_encs.shape[0], 1)), oh_encs), axis=1)\n",
    "oh_encs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "3ebfdf8b-8531-46a6-bb2f-a7966f19e1a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 0])"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encs.argmax(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "3e95c8b4-de53-438a-b0c5-59bdd2474406",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Female', 'Male'], dtype='<U6')"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "unique_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "7c7bb153-0a08-40ca-a436-fc0ee8b22640",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Female', 'Male', 'UNKNOW'], dtype='<U6')"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "unique_values = np.append(unique_values, 'UNKNOW')\n",
    "unique_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "46a449c4-21cf-442c-b6c2-d0e14eca97a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Female'],\n",
       "       ['Male'],\n",
       "       ['UNKNOW']], dtype='<U6')"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = unique_values[oh_encs.argmax(axis=1) - 1].reshape(-1, 1)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "30fb08e8-1390-4907-9f4b-70085bfce81b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Female', 'Female'],\n",
       "       ['Male', 'Male'],\n",
       "       ['UNKNOW', 'UNKNOW']], dtype='<U6')"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.concatenate([a, a], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "12b75528-d157-45b8-b486-4bbaf6f78cbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Female'],\n",
       "       ['Male'],\n",
       "       ['UNKNOW'],\n",
       "       ['Female'],\n",
       "       ['Male'],\n",
       "       ['UNKNOW']], dtype='<U6')"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.concatenate([a, a], axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e855ab6b-3244-46bc-a9af-9449690d2208",
   "metadata": {},
   "outputs": [],
   "source": [
    "from preprocessing import OneHotEncoder\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5853379f-4be5-4343-b278-566abcb549b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = np.array([['Male', 1], ['Female', 3], ['Female', 2]])\n",
    "oh_encoder = OneHotEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "53f51c18-1948-4fd2-8b7b-92abcec1d6f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<preprocessing.OneHotEncoder at 0x110efbfd0>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encoder.fit(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "043a6f24-de70-438c-a1d9-36faf7868976",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 1., 1., 0., 0.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 1., 0.]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encoder.transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5a1f10c3-c69b-46d1-ae9d-e2e862ad127c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 1., 0., 0.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_ = np.array([['MalFe', 1], ['Female', 3], ['Female', 4]])\n",
    "oh_encoder.transform(X_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d7fc480e-12e3-4e7c-86e1-5831b0034493",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Male', '1'],\n",
       "       ['Female', '3'],\n",
       "       ['Female', '2']], dtype='<U21')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oh_encoder.inverse_transform(oh_encoder.transform(X))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b893c54-58d9-4ef1-91ba-748112bc84ae",
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
