{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0f731e93-6cae-44df-a02e-a1bad6c91212",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please add 9 digits in the list\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def calculate(testList):\n",
    "    try: \n",
    "        a = np.array(testList)\n",
    "        a = a.reshape(3, 3)  \n",
    "        m1 = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean().tolist()]\n",
    "        v1 = [a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.var().tolist()]\n",
    "        st1 = [a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.std().tolist()]\n",
    "        ma1 = [a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.max().tolist()]\n",
    "        mi1 = [a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.min().tolist()]\n",
    "        sum1 = [a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.sum().tolist()]\n",
    "        Dict = {'mean': m1,'variance':v1, 'standard deviation': st1, 'max': ma1, 'min': mi1, 'sum': sum1}\n",
    "        print(Dict)\n",
    "    except ValueError:\n",
    "        print(\"Please add 9 digits in the list\")\n",
    "\n",
    "calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dff84c46-751d-453a-bfd7-fc963088c6ab",
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
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
