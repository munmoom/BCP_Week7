{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled36.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMsdqDEfU7tnC+B27YaC41+",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week7/blob/main/3-1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N_FmCB5QQ6z1"
      },
      "outputs": [],
      "source": [
        "import csv\n",
        "with open('/content/average-latitude-longitude-countries.csv' , 'r') as f:\n",
        "  rd = csv.reader(f)\n",
        "\n",
        "  list_a=[]\n",
        "  list_b=[]\n",
        "  list1=[]\n",
        "  list2=[]\n",
        "  i=0\n",
        "  for row in rd:  \n",
        "    if i == 0:\n",
        "      del row\n",
        "      i += 1    \n",
        "    else:\n",
        "      list_a=[str(row[0]), str(row[1])]\n",
        "      list_b=[str(row[0]), [float(row[2]), float(row[3])]]\n",
        "      list1.append(list_a)\n",
        "\n",
        "      list2.append(list_b)\n",
        "list1=tuple(list1)\n",
        "list2=tuple(list2)  \n",
        "  \n",
        "print(list1)\n",
        "print(list2)\n"
      ]
    }
  ]
}