#include "lists.h"
#include <stdlib.h>
/**
* check_cycle - functn checks presence of cycle in list
* @list: pointer to list
* Return: an integer value
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
