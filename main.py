# Create the following piece of code:
# If x > 200, print out "Big";
# If x > 100 and x <= 200, print out "Average"; and
# If x <= 100, print out "Small".
# Use the if, elif, and else keywords in your code.

# x=99
# if x > 200:
#     print('Big')
# elif 200 >= x > 100:
#     print('Average')
# else:
#     print('Small')
#
# # You can achieve this by traversing the array in a spiral order. Here's a Python function to do that:
# def snail(snail_map):
#     result = []
#     while snail_map:
#         result += snail_map.pop(0)
#         if snail_map and snail_map[0]:
#             for row in snail_map:
#                 result.append(row.pop())
#         if snail_map:
#             result += snail_map.pop()[::-1]
#         if snail_map and snail_map[0]:
#             for row in snail_map[::-1]:
#                 result.append(row.pop(0))
#     return result
#
#  # Example usage:
# snail_map = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result = snail(snail_map)
# print(result)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# def distance_from_zero(num):
#     if type(num)==int:
#         print(abs(num))
#     else:
#         print('Not Possible')
#
# distance_from_zero(-10)
# distance_from_zero('cat')

# Create a range object with start=1, stop=10, step=2
my_range = range(1, 10, 2)

# Convert the range to a list
# my_list = list(my_range)
#
# # Display the list
# print(my_list)
#
# list = list(range(0,11))
# print(list)

import numpy
import pandas
import matplotlib
import seaborn
import sklearn
import scipy
import statsmodels.api as sm
import math

# raw_data = pandas.read_csv('1.03.+Dummies.csv')
# data = raw_data.copy()
# data['Attendance'] = data['Attendance'].map({'Yes': 1, 'No': 0})
# print(data)
# print('Ok')

# list = [12, 24, 37, 42, 55, 62, 72, 77, 246, 592]
# mean = numpy.mod(list)
# print(mean)


# Python int
python_integer = 42

# NumPy int64
numpy_int64 = numpy.int64(42)

# Check types
print(type(python_integer))  # <class 'int'>
print(type(numpy_int64))     # <class 'numpy.int64'>

print(python_integer==numpy_int64)

list = '626 58 557 232 589 221 899 144 348 193 593 406 213 462 510 103 388 725 699 69 432 647 855 958 644 525 654 5 118 441 608 845 132 188 605 828 995 717 443 773 672 389 357 535 493 411 924 95 849 374 121 657 740 471 102 980 287 105 934 771 212 323 479 674 662 803 706 852 612 430 796 315 197 880 161 611 2 724 636 29 489 304 41 693 92 76 518 169 884 842 815 321 300 972 78 522 986 21 810 124 93 912 200 984 139 408 136 264 54 448 57 492 625 642 123 223 913 588 438 801 234 74 423 726 718 966 888 39 988 553 534 402 106 405 61 218 503 109 698 393 951 686 764 88 207 607 67 783 299 971 307 457 886 205 875 715 486 298 247 330 149 569 504 18 904 746 794 836 707 289 848 681 65 497 755 293 987 989 449 543 349 692 606 499 895 635 600 704 292 658 928 50 376 937 490 616 751 708 793 13 459 173 96 470 319 226 918 26 539 782 456 936 501 574 669 391 371 942 252 325 404 791 709 561 390 716 614 921 682 827 28 688 841 277 974 313 196 345 472 104 49 259 419 396 973 217 8 723 11 246 407 442 166 133 378 98 645 260 610 623 113 819 530 533 64 853 56 476 638 491 949 508 422 469 649 560 604 416 463 414 227 283 494 97 455 350 858 450 631 158 898 265 127 395 285 222 261 831 953 421 683 72 652 240 772 159 84 403 620 434 347 619 908 273 12 100 817 991 215 865 294 882 680 762 125 174 16 963 613 225 154 6 982 410 843 170 191 870 671 230 413 235 20 997 86 795 737 363 400 778 632 437 679 184 392 317 211 385 210 427 206 153 108 366 431 361 249 628 311 532 208 185 767 821 216 122 239 923 190 648 337 967 306 34 327 832 749 809 353 721 655 447 35 439 444 812 328 876 446 594 869 697 627 730 182 689 914 362 577 867 685 474 650 540 380 7 224 956 834 629 397 756 742 295 251 566 99 917 562 992 524 916 355 575 370 231 148 258 329 587 571 275 743 808 769 929 597 813 272 338 663 271 27 180 112 506 382 269 550 665 199 172 826 538 466 46 145 302 975 952 267 748 705 417 847 202 979 38 583 775 926 900 750 883 818 354 451 110 3 192 998 436 107 741 47 160 45 909 528 150 384 994 25 426 91 70 201 766 79 87 601 360 195 55 274 477 387 429 710 316 960 164 147 719 375 4 955 581 521 189 536 137 846 839 312 519 17 256 480 253 177 548 157 595 135 198 52 851 978 454 340 996 563 777 985 977 373 507 270 111 931 722 820 187 807 386 19 738 944 653 881 941 399 358 114 168 757 428 163 22 596 765 351 126 526 959 850 425 254 517 646 691 296 339 171 101 833 433 780 165 435 744 736 584 576 694 146 877 186 342 483 167 968 969 580 554 383 291 117 326 887 310 268 515 811 786 155 71 394 970 266 927 352 609 547 467 248 214 346 758 925 816 178 141 727 343 567 896 957 356 9 377 907 621 659 520 77 130 915 788 344 284 868 203 523 673 511 372 496 823 229 602 500 209 910 906 667 720 785 194 468 943 80 591 73 1 932 729 860 367 922 897 947 42 711 63 892 305 544 475 368 162 630 862 559 797 531 549 412 990 768 687 44 981 702 893 814 670 131 301 481 732 806 586 861 615 864 369 854 484 701 241 759 152 482 398 805 502 677 889 220 276 341 24 485 453 781 598 331 837 0 835 824 761 950 599 537 333 324 420 464 332 739 804 731 878 10 244 282 873 930 440 735 776 666 579 660 745 633 840 902 219 51 799 552 318 964 452 236 582 948 134 911 32 233 140 59 903 286 863 119 747 204 800 424 381 825 75 94 890 637 763 787 514 558 734 488 728 792 142 498 939 643 242 556 545 505 622 678 940 690 684 288 461 33 712 322 60 551 36 237 592 564 53 85 954 754 359 572 830 516 465 624 445 255 703 938 713 857 529 66 90 945 965 844 901 473 308 920 664 83 478 364 336 641 527 243 401 418 415 334 31 790 661 603 314 263 879 872 640 14 696 409 639 590 753 871 115 181 585 789 565 675 838 297 128 859 774 365 495 541 573 179 866 555 542 48 993 779 933 156 320 784 138 961 798 116 733 770 829 891 946 651 656 82 695 89 668 279 822 262 151 250 228 976 634 30 335 379 183 760 617 509 983 176 40 37 752 487 999 935 175 700 257 290 129 23 238 280 120 714 43 874 15 309 513 278 856 458 676 81 143 68 546 460 802 512 245 618 905'

list = list.split(' ')
num_list = [int(item) for item in list]
sorted_num_list = sorted(num_list)
print(sorted_num_list)

# for index in range(1, len(sorted_num_list)-1):
#     print(f'{sorted_num_list[index]}:{sorted_num_list[index+1]}')
#     if (sorted_num_list[index+1] - sorted_num_list[index]) != 1:
#         print(sorted_num_list[index] + 1)

missing_nums = [sorted_num_list[index] + 1 for index in range(1, len(sorted_num_list)-1) if (sorted_num_list[index+1] - sorted_num_list[index]) != 1]
print(missing_nums)

