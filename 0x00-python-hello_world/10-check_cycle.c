#include "lists.h"

/*
* check_cycle - check if in a linked list there's a cycle
* @list: single-linked list
*
* Return: 0 if there's no cycle or 1 if there's
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;
	
	slow_p = list;
	fast_p = list;

	if (list == NULL)
		return (0);

	while (fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
			return (1);
	}	
	return (0);
}
