{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled33.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOcQWjxmM7twWzyrJsnC7ZP",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week7/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qVb8Woy37prv"
      },
      "outputs": [],
      "source": [
        "def merge(a,b):\n",
        "  F = open('/content/b', 'w')\n",
        "  i=0\n",
        "  num=len(a)\n",
        "  for i in range(0,num):\n",
        "    f = open(f\"/content/{a[i]}\",'r')\n",
        "    F.write(f.read())\n",
        "    i += 1\n",
        "    f.close()\n",
        "  F.close()"
      ]
    }
  ]
}