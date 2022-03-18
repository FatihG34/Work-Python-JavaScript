{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3781239f",
   "metadata": {},
   "source": [
    "``` python\n",
    "\n",
    "while condition1 :\n",
    "    body1\n",
    "    while condition2 :\n",
    "        body2\n",
    "        break  # ikinci (içteki) while döngüsünden çıkartır.\n",
    "    break  # ilk (dıştaki) while döngüsünden çıkartır.\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98158085",
   "metadata": {},
   "outputs": [],
   "source": [
    "number = input(\"Please enter a number : \")\n",
    "while not number.isdigit() :\n",
    "    print(input(\"It is an invalid entry. Don't use non-numeric, float, or negative values!\"))\n",
    "    break\n",
    "number1 = input(\"Please enter a number : \")\n",
    "nmbr = list(number1)\n",
    "arms_nmbr1 = 0\n",
    "arms_nmbr2 = number1\n",
    "while arms_nmbr2 > 0:\n",
    "    digit = arms_nmbr2 % 10\n",
    "    arms_nmbr1 += pow(digit, number1)\n",
    "    arms_nmbr2 //= 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36a17ab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "number.isnumeric()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fea2774b",
   "metadata": {},
   "outputs": [],
   "source": [
    "5**3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7f149ad1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number : 9474\n",
      "9474 is not an Armstrong number\n"
     ]
    }
   ],
   "source": [
    "n = input(\"Please enter a number : \")\n",
    "while not n.isdigit() :\n",
    "    print(\"It is an invalid entry. Don't use non-numeric, float, or negative values!\")\n",
    "    n = input(\"Please enter a number : \")\n",
    "    \n",
    "#initialize the sum\n",
    "r = len(n)\n",
    "\n",
    "s = 0\n",
    "\n",
    "t = int(n)\n",
    "\n",
    "while t > 0:\n",
    "\n",
    "   digit = t % 10\n",
    "\n",
    "   s += digit ** r\n",
    "\n",
    "   t //= 10\n",
    "\n",
    "\n",
    "\n",
    "# display the result\n",
    "\n",
    "if n == s:\n",
    "\n",
    "   print(n,\"is an Armstrong number\")\n",
    "\n",
    "else:\n",
    "\n",
    "   print(n,\"is not an Armstrong number\")\n",
    "\n",
    "\n",
    "\n",
    "#Output:\n",
    "\n",
    "#Enter a number: 153\n",
    "\n",
    "#153 is an Armstrong number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e7d859c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "09a24ebd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Let's find out which number is the armstrong number !!!\n",
      "Please enter a number : 9474\n",
      "9474 is not an Armstrong number\n"
     ]
    }
   ],
   "source": [
    "print(\"Let's find out which number is the armstrong number !!!\")\n",
    "\n",
    "\n",
    "while True:\n",
    "    taken_nmbr = input(\"Please enter a number : \")\n",
    "    if not taken_nmbr.isdigit():\n",
    "        print(\"It is an invalid entry. Don't use non-numeric, float, or negative values!\")\n",
    "    else:\n",
    "      break\n",
    "t = len(list(taken_nmbr))  # length of list of taken number\n",
    "\n",
    "nmbr = int(taken_nmbr)\n",
    "arm_nmbr = 0\n",
    "s = nmbr\n",
    "\n",
    "while s > 0 :\n",
    "    s= nmbr %10\n",
    "    arm_nmbr += s**t\n",
    "    nmbr //= 10\n",
    "    \n",
    "if arm_nmbr == nmbr:\n",
    "    print(arm_nmbr, \"is an Armstrong number\")\n",
    "else:\n",
    "    print(arm_nmbr, \"is not an Armstrong number\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3e94a6fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter9474\n",
      "9474 is an Armstrong number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter\"))\n",
    "\n",
    "# Changed num variable to string, \n",
    "# and calculated the length (number of digits)\n",
    "order = len(str(num))\n",
    "\n",
    "# initialize sum\n",
    "sum = 0\n",
    "\n",
    "# find the sum of the cube of each digit\n",
    "temp = num\n",
    "while temp > 0:\n",
    "   digit = temp % 10\n",
    "   sum += digit ** order\n",
    "   temp //= 10\n",
    "\n",
    "# display the result\n",
    "if num == sum:\n",
    "   print(num,\"is an Armstrong number\")\n",
    "else:\n",
    "   print(num,\"is not an Armstrong number\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "62e2b094",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type 'ok' when you are done: 45\n",
      "Type 'ok' when you are done: 2\n",
      "Type 'ok' when you are done: ok\n",
      "\n",
      "Rain-trapped area :  0\n"
     ]
    }
   ],
   "source": [
    "height = []\n",
    "\n",
    "while True:\n",
    "    num = input(\"Type 'ok' when you are done: \")\n",
    "    \n",
    "    if num != \"ok\":\n",
    "        height.append(int(num))\n",
    "    else:\n",
    "        break\n",
    "areas = 0\n",
    "max_l = max_r = 0\n",
    "l = 0\n",
    "r = len(height)-1\n",
    "while l < r:\n",
    "        \n",
    "    if height[l] < height[r]:\n",
    "           \n",
    "        if height[l] > max_l:\n",
    "            max_l = height[l]    \n",
    "        else:\n",
    "            areas += max_l - height[l]      \n",
    "        l += 1  \n",
    "    else:                \n",
    "        if height[r] > max_r:\n",
    "            max_r = height[r]       \n",
    "        else:\n",
    "            areas += max_r - height[r]       \n",
    "        r -= 1\n",
    "\n",
    "print(\"\\nRain-trapped area : \", areas)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dab932a",
   "metadata": {},
   "source": [
    "``` Aşağıda ki \n",
    "armstrong number assigment ı\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58c438ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Let's find out which number is the armstrong number !!!\")\n",
    "\n",
    "while True:\n",
    "    taken_nmbr = input(\"Please enter a number : \")\n",
    "    if not taken_nmbr.isdigit():\n",
    "        print(\"It is an invalid entry. Don't use non-numeric, float, or negative values!\")\n",
    "    else:\n",
    "      break\n",
    "nmbr = int(taken_nmbr)\n",
    "t = len(taken_nmbr)\n",
    "\n",
    "arm_nmbr = 0\n",
    "s = nmbr\n",
    "\n",
    "while s > 0 :\n",
    "  q= s %10\n",
    "  arm_nmbr += q**t\n",
    "  s = s // 10\n",
    "\n",
    "if nmbr == arm_nmbr:\n",
    "  print(arm_nmbr, \"is an Armstrong number\")\n",
    "else:\n",
    "  print(nmbr, \"is not an Armstrong number\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c71db71",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "191f4941",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e612ce3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be397f20",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17d97966",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

