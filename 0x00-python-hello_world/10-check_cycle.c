#include "lists.h"
#include <stdlib.h>
/**
* check_cycle - functn checks presence of cycle in list
* @list: pointer to list
* Return: an integer value
*/
int check_cycle(listint_t *list)
{
listint_t *p;
listint_t *support;
if (list == NULL)
return (0);
p = list->next;
while (p != NULL)
{
if (p == p->next)
return (1);
support = list;
while (support != p)
{
if (support == p->next)
return (1);
support = support->next;
}
p = p->next;
}
return (0);
}
