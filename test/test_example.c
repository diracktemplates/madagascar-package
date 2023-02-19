#include "Unity/unity.h"

void setUp(){};

void tearDown(){};

void test_example()
/*< A test example >*/
{
	TEST_PASS();
}

int main(void){

        UNITY_BEGIN();
        RUN_TEST(test_example);
        return UNITY_END();
}

