__kernel void hello_world(__global char* buffer) {
  buffer[get_global_id(0)] = 'H';
  buffer[get_global_id(0)+1] = 'e';
  buffer[get_global_id(0)+2] = 'l';
  buffer[get_global_id(0)+3] = 'l';
  buffer[get_global_id(0)+4] = 'o';
  buffer[get_global_id(0)+5] = ',';
  buffer[get_global_id(0)+6] = ' ';
  buffer[get_global_id(0)+7] = 'W';
  buffer[get_global_id(0)+8] = 'o';
  buffer[get_global_id(0)+9] = 'r';
  buffer[get_global_id(0)+10] = 'l';
  buffer[get_global_id(0)+11] = 'd';
  buffer[get_global_id(0)+12] = '!';
}
