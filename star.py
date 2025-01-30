{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number12345\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "c=input(\"enter a number\")\n",
    "print(int(c[0])+int(c[-1]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'end' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-4310e3db1ff7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'*'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'end' is not defined"
     ]
    }
   ],
   "source": [
    "for i in range(7):\n",
    "    for j in range(5):\n",
    "        print('*',end-' ') \n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * * \n",
      "* * * * * \n",
      "* * * * * \n",
      "* * * * * \n",
      "* * * * * \n",
      "* * * * * \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "for i in range(7):\n",
    "    for j in range(5):\n",
    "        print('*',end=' ') \n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-9e76d533202e>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-9e76d533202e>\"\u001b[1;36m, line \u001b[1;32m4\u001b[0m\n\u001b[1;33m    if i==a or j=b//2\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=7\n",
    "for i in range(a):\n",
    "    if i==a or j=b//2\n",
    "      print('*',end=' ')\n",
    "        else:\n",
    "            print(' ',end=' ')\n",
    "        print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*         \n",
      "  *   *   \n",
      "  * *     \n",
      "      *   \n",
      "        * \n"
     ]
    }
   ],
   "source": [
    "a=b=5\n",
    "for i in range(a):\n",
    "    for j in range(b):\n",
    "        print('*',end=' ') if i==j or i==a-j-i else print(' ',end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          \n",
      "          \n",
      "* * * * * \n",
      "      *   \n",
      "    *     \n",
      "  *       \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "b=7\n",
    "c=5\n",
    "for i in range(0 ,b):\n",
    "    for j in range(0, c):\n",
    "        if i==2 or j==6 or i==b-1 or i+j==6:\n",
    "            print(\"*\",end=\" \")\n",
    "        else:\n",
    "            print(\" \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          \n",
      "          \n",
      "*       * \n",
      "  *   *   \n",
      "    *     \n",
      "  *   *   \n",
      "*       * \n"
     ]
    }
   ],
   "source": [
    "b=7\n",
    "c=5\n",
    "for i in range(0 ,b):\n",
    "    for j in range(0, c):\n",
    "        if i-j==2 or i-j==6 or i==b or i+j==6:\n",
    "            print(\"*\",end=\" \")\n",
    "        else:\n",
    "            print(\" \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * * \n",
      "*       * \n",
      "*       * \n",
      "*       * \n",
      "*       * \n",
      "*       * \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "b=7\n",
    "c=5\n",
    "for i in range(0 ,b):\n",
    "    for j in range(0, c):\n",
    "        if i==0 or j==0 or i==b-1 or j == c-1:\n",
    "            print(\"*\",end=\" \")\n",
    "        else:\n",
    "            print(\" \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * * \n",
      "    *     \n",
      "    *     \n",
      "    *     \n",
      "    *     \n",
      "    *     \n",
      "    *     \n"
     ]
    }
   ],
   "source": [
    "b=7\n",
    "c=5\n",
    "for i in range(0 ,b):\n",
    "    for j in range(0, c):\n",
    "        if i==0 or j==2 or i == b or j == c:\n",
    "            print(\"*\",end=\" \")\n",
    "        else:\n",
    "            print(\" \",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
