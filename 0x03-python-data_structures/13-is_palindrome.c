#include "lists.h"

/**
 *is_palindrome - function to detect if a single list is a palindrome
 *@head: head of the single linked list
 *Return: 0 if is not, 1 if is it
 */
int is_palindrome(listint_t **head)
{
	void *origin;
	int len = 0, tmp_array[1000000], i = 0;

	if (*head == NULL)
		return (1);
	origin = *head;
	while (*head != NULL)
	{
		*head = (*head)->next;
		len++;
	}
	len--;
	*head = origin;
	/*tmp_array = malloc(((len + 1) / 2) * sizeof(int));*/
	for (i = 0; i <= len; i++)
	{
		if (i <= (len / 2))
		{
			tmp_array[i] = (*head)->n;
			*head = (*head)->next;
		}
		else
		{
			if (tmp_array[len - i] != (*head)->n)
			{
				/*free(tmp_array);*/
				*head = origin;
				return (0);
			}
			*head = (*head)->next;
		}
	}
	/*free(tmp_array);*/
	*head = origin;
	return (1);
}
