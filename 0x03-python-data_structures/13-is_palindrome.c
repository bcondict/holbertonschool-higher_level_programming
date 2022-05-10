#include "lists.h"

/**
* reverse_listint - checks a linked list in reverse
* @head: pointer of head node
*
* Return: a pointer to the last node int linked list
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
* is_palindrome - check if a single linked list is a palindrome
* @head: pointer of head node
*
* Return: 1 in success, 0 on failure
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = NULL, *fast = NULL;

	slow = *head;
	fast = *head;

	if (!*head || !(*head)->next)
		return (1);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	reverse_listint(&slow);

	fast = *head;

	while (fast && slow)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}
