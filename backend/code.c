#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

/*Practice for upcomming C(PPS) Exam, aka Midsem,
Its 12:01 pm and I have the test at 2:00pm:),,,
WISH ME LUCK?*/
int test_output()
{
    int i = 0, x = 0;
    for (i = 1; i < 5; ++i)
    {
        if (i % 2 == 1)
            x += i;
        else
            x--;
        printf("%d\n", x);
    }
    return 0;
}

int PEMDAS()
{
    int a = 5 * (10 / 5 + (7 * 6 - 3) % (6 + 5 - 2));
    printf("%d", a);
    return 0;
}

char switch_case(char x)
{
    printf("input = %c\n", x);
    switch (x)
    {
    case 'a':
        printf("vowel\n");
        break;
    case 'e':
        printf("vowel\n");
        break;
    case 'i':
        printf("vowel\n");
        break;
    case 'o':
        printf("vowel\n");
        break;
    case 'u':
        printf("vowel\n");
        break;
    default:
        printf("consonant\n");
    }
}

int prime_num_check()
{
    int i, n, f = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    if (n == 0 || n == 1)
        printf("%d is neither prime not composite");
    else
    {
        if (n % 2 == 0)
            f = 1;
        else
        {
            for (i = 2; i < n; i++)
            {
                if (n % i == 0)
                    f = 1;
            }
        }
    }
    if (f == 0)
        printf("prime\n");
    else
        printf("Composite\n");
}

/*Code from this point onwards is normal practice*/

int one_nth_sum()
{
    int n;
    float sum, i;
    printf("Enter a integer: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        sum += (1 / i);
    }
    printf("%0.4f\n", sum);
}

void array_insertion()
{
    int n, pos, size, i;
    int array[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Enter custom position: ");
    scanf("%d", &pos);
    printf("Enter size of array: ");
    scanf("%d", &size);
    size_t sizo = sizeof(array) / sizeof(array[0]);
    array[0] = n;
    array[sizo - 1] = n;
    array[pos - 1] = n;
    printf("[");
    for (i = 0; i < sizo; i++)
        printf("%d ", array[i]);
    printf("]\n");
    printf("%d", sizo);
}

int reverse_array()
{
    int i, j, temp, size;

    printf("Enter size of array: ");
    scanf("%d", &size);

    int array[size];

    for (i = 0; i < size; i++)
    {
        printf("Enter Element %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    for (j = 0; j < i; j++)
    {
        printf("%d ", array[j]);
    }

    for (i = 0, j = size - 1; i < size / 2; i++, j--)
    {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    printf("\n");

    for (i = 0; i < size; i++)
    {
        printf("%d ", array[i]);
    }

    printf("\n");

    return 0;
}

void palindrome()
{
    int i, j, temp, size;
    // If Word is predefined then uncomment the below line
    char word[] = {"LIVE"};

    // If word is user input then uncomment the below segment
    /*
    char word[20];
    printf("Enter a word: ");
    scanf("%s", &word);
    */

    size = sizeof(word) / sizeof(word[0]);

    for (j = 0; j < size; j++)
    {
        printf("%c", word[j]);
    }

    for (i = 0, j = size - 1; i < size / 2; i++, j--)
    {
        temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }

    printf("\n");

    for (i = 0; i < size; i++)
    {
        printf("%c", word[i]);
    }

    printf("\n");
}

void linear_search(int n)
{
    int i, array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(array) / sizeof(array[0]);
    bool f;
    for (i = 0; i <= size; i++)
    {
        if (array[i] == n)
        {
            printf("Element found on position %d\n", array[i]);
            f = 1;
            break;
        }
    }
    if (!f)
    {
        printf("Element not found");
    }
}

void binary_search(int n)
{
    int left, right, mid, array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(array) / sizeof(array[0]);
    bool f;
    left = 0;
    right = size - 1;

    while (left <= right)
    {
        mid = (left + right) / 2;

        if (mid == n)
        {
            printf("Element found at position %d\n", mid);
            f = 1;
            break;
        }
        else if (mid < n)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    if (!f)
    {
        printf("Element not found\n");
    }
}

int bubble_sort()
{
    // code here
}

void Dynamic_array_in_C_HR()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);

    int type_of_query;
    scanf("%d", &type_of_query);

    int shelf[total_number_of_shelves][100];
    int z = 0;

    while (type_of_query--)
    {
        if (type_of_query == 1)
        {
            int x, y;
            scanf("%d%d", &x, &shelf[x][z]);
            printf("\n%d\n", shelf[z][x]);
            z++;
        }
        if (type_of_query == 2)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            printf("\n%d\n", shelf[x][y]);
        }
    }
}

int greatest(int a, int b, int c)
{
    return ((a > b) && (a > c)) ? a : ((b > c) && (b > a)) ? b
                                                           : c;
}

void strsort()
{
    char *string;
    string = malloc(255 * sizeof(char));
    scanf("%s", string);
    int size = strlen(string);
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < size - 1; j++)
        {
            if (string[i] > string[j])
            {
                char temp = string[i];
                string[i] = string[j];
                string[j] = temp;
            }
        }
    }
    printf("%s\n", string);
}

void hacehdec()
{
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int array[n];
    int i, j, temp;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }

    for (i = 0; i < (n / 2) - 1; i++)
    {
        for (j = 0; j < (n / 2) - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    for (i = n; i > n / 2; i--)
    {
        for (j = n; j > n / 2 - 1; j--)
        {
            if (array[j] > array[j - 1])
            {
                temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
            }
        }
    }

    for (i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
}

void anagram()
{
    char word1[255];
    char word2[255];
    printf("Enter word 1: ");
    scanf("%s", &word1);
    printf("Enter word 2: ");
    scanf("%s", &word2);
    int check1[27] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, check2[27] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int check = 1;
    if (strlen(word1) != strlen(word2))
    {
        printf("Nah");
    }
    else if (!strcmp(word1, word2))
    {
        printf("Yeah!");
    }
    else
    {
        for (int i = 0; i < strlen(word1); i++)
        {
            switch (word1[i])
            {
            case 'a':
                check1[0] += 1;
                break;
            case 'b':
                check1[1] += 1;
                break;
            case 'c':
                check1[2] += 1;
                break;
            case 'd':
                check1[3] += 1;
                break;
            case 'e':
                check1[4] += 1;
                break;
            case 'f':
                check1[5] += 1;
                break;
            case 'g':
                check1[6] += 1;
                break;
            case 'h':
                check1[7] += 1;
                break;
            case 'i':
                check1[8] += 1;
                break;
            case 'j':
                check1[9] += 1;
                break;
            case 'k':
                check1[10] += 1;
                break;
            case 'l':
                check1[11] += 1;
                break;
            case 'm':
                check1[12] += 1;
                break;
            case 'n':
                check1[13] += 1;
                break;
            case 'o':
                check1[14] += 1;
                break;
            case 'p':
                check1[15] += 1;
                break;
            case 'q':
                check1[16] += 1;
                break;
            case 'r':
                check1[17] += 1;
                break;
            case 's':
                check1[18] += 1;
                break;
            case 't':
                check1[19] += 1;
                break;
            case 'u':
                check1[20] += 1;
                break;
            case 'v':
                check1[21] += 1;
                break;
            case 'w':
                check1[22] += 1;
                break;
            case 'x':
                check1[23] += 1;
                break;
            case 'y':
                check1[24] += 1;
                break;
            case 'z':
                check1[25] += 1;
                break;
            }
        }
        for (int i = 0; i < strlen(word2); i++)
        {
            switch (word2[i])
            {
            case 'a':
                check2[0] += 1;
                break;
            case 'b':
                check2[1] += 1;
                break;
            case 'c':
                check2[2] += 1;
                break;
            case 'd':
                check2[3] += 1;
                break;
            case 'e':
                check2[4] += 1;
                break;
            case 'f':
                check2[5] += 1;
                break;
            case 'g':
                check2[6] += 1;
                break;
            case 'h':
                check2[7] += 1;
                break;
            case 'i':
                check2[8] += 1;
                break;
            case 'j':
                check2[9] += 1;
                break;
            case 'k':
                check2[10] += 1;
                break;
            case 'l':
                check2[11] += 1;
                break;
            case 'm':
                check2[12] += 1;
                break;
            case 'n':
                check2[13] += 1;
                break;
            case 'o':
                check2[14] += 1;
                break;
            case 'p':
                check2[15] += 1;
                break;
            case 'q':
                check2[16] += 1;
                break;
            case 'r':
                check2[17] += 1;
                break;
            case 's':
                check2[18] += 1;
                break;
            case 't':
                check2[19] += 1;
                break;
            case 'u':
                check2[20] += 1;
                break;
            case 'v':
                check2[21] += 1;
                break;
            case 'w':
                check2[22] += 1;
                break;
            case 'x':
                check2[23] += 1;
                break;
            case 'y':
                check2[24] += 1;
                break;
            case 'z':
                check2[25] += 1;
                break;
            }
        }
        for (int i = 0; i < 26; i++)
        {
            if (check1[i] != check2[i])
            {
                printf("Nah\n");
                check = 0;
                break;
            }
        }
        if (check == 1)
        {
            printf("Yeah\n");
        }
    }
}
void main()
{
    // call the function for the wanted program
    reverse_array();
}
