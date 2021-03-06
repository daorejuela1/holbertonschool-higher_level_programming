#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a cycle exist in a linked list
 * @list: list to check if has a cycle or not
 *
 * Return: 1 if there's a cycle 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *fast;
	if (list != NULL && list->next !=NULL && list->next->next != NULL)
	{
		fast = list->next->next;
	}
	else
	{
		return (0);
	}
	while (fast->next != NULL  && fast->next->next != NULL)
	{
		if (fast == list)
			return (1);
		list = list->next;
		fast = fast->next->next;
	}
	return (0);
}
