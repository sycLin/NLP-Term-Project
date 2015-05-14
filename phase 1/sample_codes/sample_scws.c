#include <stdio.h>
#include <scws.h>

int main() {
	scws_t s;
	scws_res_t res, cur;
	char sample_text[200] = "Hello, 我名字叫李逼曲是一个中国人, 我有时买Q币来玩, 我还听说过C#语言";

	if( !(s = scws_new()) ) {
		fprintf(stderr, "ERROR: cannot init the scws: scws_new()\n");
		exit(1);
	}

	scws_set_charset(s, "utf8");
	scws_set_dict(s, "/usr/local/scws/etc/dict.utf8.xdb", SCWS_XDICT_XDB);
	scws_set_rule(s, "/usr/local/scws/etc/rules.utf8.ini");

	scws_send_text(s, sample_text, strlen(sample_text));
	
	while(res = cur = scws_get_result(s)) {
		while(cur != NULL) {
			fprintf(stdout, "WORD: %.*s/%s (IDF = %4.2f)\n", cur->len, sample_text+cur->off, cur->attr, cur->idf);
			cur = cur->next;
		}
		scws_free_result(res);
	}
	scws_free(s);
}
