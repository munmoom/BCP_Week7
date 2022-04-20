{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled31.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPgUus+uqSRLIKvKPsw7gxz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week7/blob/main/202255127-1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "msg=\"\"\"\n",
        "1.새로 만들기\n",
        "2.가계부 보기\n",
        "3.수입 추가하기\n",
        "4.지출 추가하기\n",
        "\"\"\"\n",
        "print(msg)\n",
        "\n",
        "def create():\n",
        "  f = open('/content/가계부 만들기/account_book.txt','r')\n",
        "  f.close()\n",
        "\n",
        "def peruse():\n",
        "  f = open('/content/가계부 만들기/account_book.txt','r')  \n",
        "  data = f.read()\n",
        "  print(data)\n",
        "  f.close()\n",
        "\n",
        "def add_income():\n",
        "  import datetime\n",
        "  income = input('[수입] :')\n",
        "  how1 = input('(경로) :')\n",
        "  with open('/content/가계부 만들기/account_book.txt','a') as f:\n",
        "    f.write(f'[수입]{datetime.datetime.now()} {income}원 {how1}\\n')\n",
        "\n",
        "def add_payout():\n",
        "   import datetime\n",
        "   payout = input('[지출] :')\n",
        "   how2 = input('(경로)')\n",
        "   with open('/content/가계부 만들기/account_book.txt','a') as f:\n",
        "     f.write(f'[지출]{datetime.datetime.now()} {payout} {how2}\\n')\n",
        "\n",
        "\n",
        "while True:\n",
        "  menu = int(input(\"menu:\"))\n",
        "  if menu == 1:\n",
        "    print(\"새로 만들기\")\n",
        "    create()\n",
        "  elif menu ==2:\n",
        "    print(\"가계부 보기\")\n",
        "    peruse()\n",
        "  elif menu ==3:\n",
        "    print(\"수입 추가하기\")\n",
        "    add_income()\n",
        "  elif menu ==4:\n",
        "    print(\"지출 추가하기\")\n",
        "    add_payout()\n",
        "  else:\n",
        "    print('가계부 종료') \n",
        "    break       "
      ],
      "metadata": {
        "id": "wBxu11ZPfzzT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "msg=\"\"\"\n",
        "1.새로 만들기\n",
        "2.가계부 보기\n",
        "3.수입 추가하기\n",
        "4.지출 추가하기\n",
        "\"\"\"\n",
        "print(msg)\n",
        "\n",
        "def create():\n",
        "  import csv\n",
        "  f = open('/content/가계부 만들기/account_book.csv','w', encoding='utf8')\n",
        "  f.close()\n",
        "\n",
        "def peruse():\n",
        "  import csv\n",
        "  f = open('/content/가계부 만들기/account_book.csv','r', encoding='utf8')  \n",
        "  data = csv.reader(f)\n",
        "  for row in data:\n",
        "    row = ', '.join(row)\n",
        "    row = row.replace(', ','')\n",
        "    print(row)\n",
        "  f.close()\n",
        "\n",
        "def add_income():\n",
        "  import datetime\n",
        "  import csv\n",
        "  income = input('[수입] :')\n",
        "  how1 = input('(경로) :')\n",
        "  with open('/content/가계부 만들기/account_book.csv','a') as f:\n",
        "    wr = csv.writer(f)\n",
        "    wr.writerow(f'[수입]{datetime.datetime.now()} {income}원 {how1}\\n')  \n",
        "\n",
        "  def add_payout():\n",
        "   import datetime\n",
        "   import csv\n",
        "   payout = input('[지출] :')\n",
        "   how2 = input('(경로) :')\n",
        "   with open('/content/가계부 만들기/account_book csv','a') as f:\n",
        "     wr = csv.writer(f)\n",
        "     wr.writerow(f'[지출]{datetime.datetime.now()} {payout}원 {how2}\\n')  \n",
        "\n",
        "while True:\n",
        "  menu = int(input(\"menu:\"))\n",
        "  if menu == 1:\n",
        "    print(\"새로 만들기\")\n",
        "    create()\n",
        "  elif menu ==2:\n",
        "    print(\"가계부 보기\")\n",
        "    peruse()\n",
        "  elif menu ==3:\n",
        "    print(\"수입 추가하기\")\n",
        "    add_income()\n",
        "  elif menu ==4:\n",
        "    print(\"지출 추가하기\")\n",
        "    add_payout()\n",
        "  else:\n",
        "    print('가계부 종료') \n",
        "    break   "
      ],
      "metadata": {
        "id": "CkOYtJj6p0gv"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}