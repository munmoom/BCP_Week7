{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled38.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPP0TnzigKzsE400SvLmoGr",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_Week7/blob/main/3-2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "myshjTmDTMXS"
      },
      "outputs": [],
      "source": [
        "import csv\n",
        "with open('/content/average-latitude-longitude-countries.csv' , 'r') as f:\n",
        "  rd = csv.reader(f)\n",
        "  dic={}\n",
        "  i=0\n",
        "  for row in rd:  \n",
        "    if i == 0:\n",
        "      del row\n",
        "      i += 1   \n",
        "    else:\n",
        "      dic[str(row[0])] = str(row[1])\n",
        "\n",
        "dic[input()]"
      ]
    }
  ]
}