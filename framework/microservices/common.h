/* Base values for various magic numbers and enums */

#ifndef COMMON_H
#define COMMON_H

#include "../include/types.h"
#include "../user_services.h"


#define GENERATE_PROVIDER_HANDLE(serviceName, microservice, accessPattern) \
  serviceName##_service_generate_##microservice##_provider_handle(accessPattern)

#define TRANSFER_SIZE 10 //RDMA-based data pull size
#define ARRAY_SIZE 1000 //Size of array being copied in memory
#define COMPUTE_CYCLES 1000000 //Number of compute cycles
#define FILE_SIZE 10000 //I/O file size
#define NUM_REQUESTS 100 //Total number of requests generated from client
#define INVERSE_REQUEST_RATE 100000 //Controls sleeptime between individual requests, thus inversely affecting request rate generated from client

#endif