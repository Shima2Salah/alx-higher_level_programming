#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - adds a new node in a sort list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *iterator = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (iterator->next)
		{
			if (number <= iterator->next->n)
			{
				new->next = iterator->next;
				iterator->next = new;
				return (new);
			}
			iterator = iterator->next;
		}
	}
	new->next = NULL;
	iterator->next = new;
	return (new);
}
