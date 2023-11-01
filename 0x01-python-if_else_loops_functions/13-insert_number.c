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
listint_t *current;
current = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL)
*head = new;
else if (current->n > new->n)
{
new->next = current;
*head = new;
}
else
{
if (current->n > new->n)
new->next = current;
while (current->n < new->n)
{
if (current->next->n > new->n)
{
new->next = current->next;
current->next = new;
}
current = current->next;
}
}
return (new);
}
