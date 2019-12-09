#include "lists.h"

/**
 *check_cycle - Checks if there is a loop in a linked list
 *
 *@list: The list to check
 *
 *Return: 1 if cycle exists or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
