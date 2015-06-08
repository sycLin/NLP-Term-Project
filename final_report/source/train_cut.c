#include <stdio.h>
#include <scws.h>

#define MAX_LENGTH 1024


// to print a horizontal line with 20 '='s
void print_hr(FILE* file_stream);

int main() {
	int i;
	scws_t s;
	scws_res_t res, cur;
	char sentence[MAX_LENGTH];
	int sentence_count = 0;
	char all_pos[MAX_LENGTH][5]; // store all the POS tags of the sentence
	int pos_index = 0;

	if( !(s = scws_new()) ) {
		fprintf(stderr, "ERROR: cannot init the scws: scws_new()\n");
		exit(1);
	}

	scws_set_charset(s, "utf8");
	scws_set_dict(s, "/usr/local/scws/etc/dict.utf8.xdb", SCWS_XDICT_XDB);
	scws_set_rule(s, "/usr/local/scws/etc/rules.utf8.ini");

	while(1) {
		if(fgets(sentence, MAX_LENGTH, stdin) == NULL) break;
		sentence[strlen(sentence)-1] = '\0'; // remove the '\n' that fgets() reads
		if(sentence[0] == 'T' || sentence[0] == 'F') {
			fprintf(stdout, sentence);
			fprintf(stdout, "\n");
			continue;
		}
		if(sentence[1] == '\0' && (sentence[0] == '0' || sentence[0] == '1')) {
			fprintf(stdout, "%s\n", sentence);
			continue;
		}
		scws_send_text(s, sentence, strlen(sentence));
		// print_hr(stdout);
		// fprintf(stdout, "start parsing the %d-th sentence: %s\n", ++sentence_count, sentence);
		pos_index = 0;
		while(res = cur = scws_get_result(s)) {
			while(cur != NULL) {
				// fprintf(stdout, "WORD: %.*s/%s (IDF = %4.2f)\n", cur->len, sentence+cur->off, cur->attr, cur->idf);
				fprintf(stdout, "%.*s#%s ", cur->len, sentence+cur->off, cur->attr);
				strcpy(all_pos[pos_index++], cur->attr);
				cur = cur->next;
			}
			scws_free_result(res);
			// output the whole POS tags
			// printf("POS tags: ");
			// for(i=0; i<pos_index; i++)
				// printf("%s ", all_pos[i]);
			// printf("\n");
		}
		printf("\n");
		// print_hr(stdout);
	}

	scws_free(s);
	return 0;
}


void print_hr(FILE* stream) {
	fprintf(stream, "====================\n");
}

