#ifndef LISTS_H
#define LISTS_H

#include "stdlib.h"

/**
 * struct listint_s - singly linked list
 * @n: integer data
 * @next: next node in list
 *
 * Description: singly linked lists
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint *head);
int check_cycle(listint_t *list);

#endif
