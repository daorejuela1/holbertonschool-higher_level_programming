#include "lists.h"
/**
 *insert_node - function that inserts a node in a sorted list
 *@head: pointer to the first node of the list
 *@number: int to add in the new node
 *Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ini_node = NULL, *new_node = NULL;
	listint_t *prev_node = NULL;

	if (head == NULL)
		return (NULL);
	ini_node = *head;
	while (*head != NULL)
	{
		prev_node = *head;
		*head = (*head)->next;
		if (*head != NULL && (*head)->n >= number)
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
			{
				*head = ini_node;
				return (NULL);
			}
			new_node->n = number;
			new_node->next = *head;
			prev_node->next = new_node;
			break;
		}
	}
	*head = ini_node;
	return (new_node);
}
