#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to the start of the node
 * Return: 0 if theres no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *initial, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	initial = list;
	check = initial->next;

	while (initial != NULL && check->next != NULL
			&& check->next->next != NULL)
	{
		if (initial == check)
			return (1);
		initial = initial->next;
		check = check->next->next;
	}
	return (0);
}
