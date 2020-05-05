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
	int len, i, n, offset = 0;
	listint_t *p = *head;

	if (*head == NULL)
		return (1);

	n = p->n;

	for (len = 0; p->next != NULL; len++)
		p = p->next;

	while (p->n == n)
	{
		offset++;
		p = *head;
		for (i = 0; i < len - offset; i++)
		{
			if (i == offset)
				n = p->n;
			p = p->next;
		}
		if (i == offset)
			n = p->n;
		if (offset > len / 2)
			return (1);
	}

	return (0);
}
