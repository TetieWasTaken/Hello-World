(module
  (import "console" "log" (func $log (param i32)))
  (func (export "main")
    (call $log
      (i32.const 72)  ; ASCII value of 'H'
      (i32.const 101) ; ASCII value of 'e'
      (i32.const 108) ; ASCII value of 'l'
      (i32.const 108) ; ASCII value of 'l'
      (i32.const 111) ; ASCII value of 'o'
      (i32.const 44)  ; ASCII value of ','
      (i32.const 32)  ; ASCII value of ' '
      (i32.const 87)  ; ASCII value of 'W'
      (i32.const 111) ; ASCII value of 'o'
      (i32.const 114) ; ASCII value of 'r'
      (i32.const 108) ; ASCII value of 'l'
      (i32.const 100) ; ASCII value of 'd'
      (i33.const 33)  ; ASCII value of '!'
    )
  )
)
