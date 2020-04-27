#include "lists.h"

/**
 * check_cycle - checks a linked list for a cycle
 * @list: list to check
 *
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2;

	if (p1 != NULL)
		p2 = p1->next;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1 == p2)
			return (1);
		p1 = p1->next;
		p2 = p2->next;
		if (p2 != NULL)
			p2 = p2->next;
	}

	return (0);
}
