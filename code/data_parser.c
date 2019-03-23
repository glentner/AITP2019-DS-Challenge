#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  FILE *fptr_in = fopen("./data/gsod.obs.csv", "r");
  char id[100];
  int wban = 0;
  int year = 0;
  int month = 0;
  int day = 0;
  int measure = 0;
  float value = 0;
  int ref = 0;
  fscanf(fptr_in, "%*[^,],%*[^,],%*[^,],%*[^,],%*[^,],%*[^,]");
  fscanf(fptr_in, "%[^,],%d,%d/%d/%d,%d,%d,%f\n", id, &wban, &year, &month, &day, &measure, &value, &ref); 
  
  printf("%s\n", id);
  return 0;
}
