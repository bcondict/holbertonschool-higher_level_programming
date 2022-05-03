#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	if (list == NULL)
		return (0);

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
			return (1);
	}	
	return (0);
}
