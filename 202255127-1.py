{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled31.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPTSYFKY+YEh4YmlzlMN4zE",
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 814
        },
        "id": "wBxu11ZPfzzT",
        "outputId": "535687cf-0f40-4e0d-c32c-067436cb7d0e"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "1.새로 만들기\n",
            "2.가계부 보기\n",
            "3.수입 추가하기\n",
            "4.지출 추가하기\n",
            "\n",
            "menu:3\n",
            "수입 추가하기\n",
            "[수입] :150000\n",
            "(경로)용돈\n",
            "menu:2\n",
            "가계부 보기\n",
            "[수입]2022-04-20 11:02:19.836490 150000 용돈\n",
            "\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    728\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 729\u001b[0;31m                 \u001b[0mident\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreply\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstdin_socket\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    730\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/jupyter_client/session.py\u001b[0m in \u001b[0;36mrecv\u001b[0;34m(self, socket, mode, content, copy)\u001b[0m\n\u001b[1;32m    802\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 803\u001b[0;31m             \u001b[0mmsg_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_multipart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcopy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    804\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mzmq\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mZMQError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/zmq/sugar/socket.py\u001b[0m in \u001b[0;36mrecv_multipart\u001b[0;34m(self, flags, copy, track)\u001b[0m\n\u001b[1;32m    624\u001b[0m         \"\"\"\n\u001b[0;32m--> 625\u001b[0;31m         \u001b[0mparts\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mflags\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcopy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtrack\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtrack\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    626\u001b[0m         \u001b[0;31m# have first part already, only loop while more to receive\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket.Socket.recv\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket.Socket.recv\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket._recv_copy\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/zmq/backend/cython/checkrc.pxd\u001b[0m in \u001b[0;36mzmq.backend.cython.checkrc._check_rc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: ",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-12-dcd2c30e4377>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 35\u001b[0;31m   \u001b[0mmenu\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"menu:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     36\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mmenu\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"새로 만들기\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    702\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    703\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 704\u001b[0;31m             \u001b[0mpassword\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    705\u001b[0m         )\n\u001b[1;32m    706\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    732\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    733\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 734\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    735\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    736\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    }
  ]
}