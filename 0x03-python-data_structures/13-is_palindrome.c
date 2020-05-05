#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a listint_t is a palindrome
 * @head: head of list to check
 *
 * Return: 0 if not palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len, i, *a;
	listint_t *p = *head;

	if (*head == NULL)
		return (1);

	for (len = 0; p->next != NULL; len++)
		p = p->next;

	a = malloc(sizeof(int) * (len + 1));
	p = *head;

	for (i = 0; i <= len; i++)
	{
		a[i] = p->n;
		p = p->next;
	}

	for (i = 0; i < len - i; i++)
	{
		if (a[i] != a[len - i])
			return (0);
	}

	return (1);
}
