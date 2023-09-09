#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i = 0, j = 0, k = 0, l = 0;
	int array[10000];

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	j = i - 1;
	while (k < j)
	{
		if (array[k] != array[j])
		l++;
		k++;
		j--;
	}
	if (l == 0)
		return (1);
	else
		return (0);
}
