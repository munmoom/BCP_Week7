{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNaR/hkB7Dho/vfa2P3nmLk",
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
      "source": [
        "t = list()\n",
        "while True:\n",
        "  add = float(input())\n",
        "  if add == 999:\n",
        "    break\n",
        "  else:\n",
        "    t.append(add)\n",
        "\n",
        "num = len(t)\n",
        "\n",
        "T = 0\n",
        "for i in t:\n",
        "  if T == 0:\n",
        "     T = i\n",
        "     continue\n",
        "  else:\n",
        "    result = i-T\n",
        "    result2 = round(result,2)\n",
        "    print(result2, end=' ')\n",
        "    T = i"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rWn12PtFjCsB",
        "outputId": "47f996d6-d08f-472d-aaf2-ebfafab7e144"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.0\n",
            "12.05\n",
            "30.25\n",
            "20\n",
            "999\n",
            "2.05 18.2 -10.25 "
          ]
        }
      ]
    }
  ]
}