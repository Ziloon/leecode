int bestClosingTime(char* customers) {
    int n = strlen(customers);
    int best_hour = 0;
    int cost_min = 0;
    int cost = 0;
    for (int j = 0; j <= n; j++) {
        if (customers[j] == 'Y') {
            cost--;
        } else {
            cost++;
        }
        if (cost < cost_min) {
            cost_min = cost;
            best_hour = j+1;
        }
    }
    return best_hour;
}