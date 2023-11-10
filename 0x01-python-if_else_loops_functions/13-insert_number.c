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
listint_t *new;
listint_t *current = *head;
if (head == NULL)
return (NULL);
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL || (*head)->n > number)
{
new->next = *head;
*head = new;
return (new);
}
while (current->n < number)
{
if (current->next == NULL)
{
current->next = new;
new->next = NULL;
return (new);
}
if (current->next->n > number)
{
new->next = current->next;
current->next = new;
}
current = current->next;
}
return (new);
}

