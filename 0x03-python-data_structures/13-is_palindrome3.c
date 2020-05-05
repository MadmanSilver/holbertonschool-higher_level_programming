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
	int len, i;
	listint_t *p = *head, *p2 = *head;

	if (*head == NULL)
		return (1);

	for (len = 0; p2->next != NULL; len++)
		p2 = p2->next;

	while (p->n == p2->n)
	{
		len--;
		p = p->next;
		p2 = *head;
		for (i = 0; i < len; i++)
			p2 = p2->next;
		if (len == 0)
			return (1);
	}

	return (0);
}
