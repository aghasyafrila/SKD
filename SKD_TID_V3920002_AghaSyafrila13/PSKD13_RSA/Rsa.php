<?php

class Rsa {

    private $p; // bilangan prima pertama
    private $q; // bilangan prima kedua
    private $n; // bilangan modulus
    private $m; // bilangan totient
    private $e; // exponen enkripsi (kunci publik untuk enkripsi)
    private $d; // exponen dekripsi (kunci privat untuk dekripsi)
    private $e_arr; // array dari e yang tersedia
    private $d_arr; // array dari sekian d yang tersedia


    function gen_key($p, $q) {
        $this->p = $p;
        $this->q = $q;
        $this->n = $p * $q;
        $this->m = ($p - 1) * ($q - 1);
        $this->gen_e($this->m);
        $this->gen_d($this->m, $this->e);
    }
    
    // function to check wether a number is a prime number
    function check_prime($num){ 
    	if ($num == 1) {
    	    return false; 
    	}
    	
    	for ($i = 2; $i <= $num / 2; $i++){ 
    		if ($num % $i == 0) {
    			return false; 
    		}
    	}
    	
    	return true; 
    } 

    // function to encrypt a text with the public key pair (e, n)
    // parameter pertama: teks yang akan dienkripsi
    // parameter kedua: kunci publik untuk enkripsi (e)
    // parameter ketiga: bilangan modulus
    function encrypt($text, $e, $n) {
        // teks di pisah per 1 karakter menjadi bentuk array
        $text_arr = str_split($text);

        foreach ($text_arr as $text_arr) {
            $ord_text = ord($text_arr); // ubah karakter ke angka desimal
            // echo "\$ord_text = $ord_text<br>";
            // echo "\$e = $e<br>";
            // echo "\$n = $n<br>";
            $chip_arr[] = bcpowmod($ord_text, $e, $n); // rumus enkripsi
        }

        $ord_chip = implode(",", $chip_arr); // array desimal disatukan dengan pemisah koma
        return $ord_chip;
    }

    // function to decrypt a text with the private key pair (d, n)
    // parameter pertama: teks yang akan didekripsi
    // parameter kedua: kunci privat untuk dekripsi (d)
    // parameter ketiga: bilangan pembagi/modulus
    function decrypt($ord_chip, $d, $n) {
        $chip_arr = preg_split("/[^0-9]/", $ord_chip); // array desimal dipisah sesuai koma
        
        foreach ($chip_arr as $chip_arr) {
            // echo "\$chip_arr = $chip_arr<br>";
            // echo "\$d = $d<br>";
            // echo "\$n = $n<br>";
            $ord_chip = bcpowmod($chip_arr, $d, $n); // rumus dekripsi
            // echo "\$ord_chip: " . $ord_chip . "<br>";
            $text_arr[] = chr($ord_chip); // ubah angka desimal ke karakter/huruf
        }
        
        $text = implode("", $text_arr); // satukan karakter tanpa pemisah
        return $text;
    }


    function gen_e($m) {
        // e[]=null;
        for ($i = 8; $i < $m; $i++) {
            if ( $this->gcd($m, $i) == 1 ) {
                $e[] = $i;
                // echo "<br>i di e=".$i;
            }
        }
        
        // $this->e = end(array_values($e));
        $this->e_arr = $e;
        $this->e = $e[0];
    }

    function gen_d($m, $e, $limit = 100) {
        $j=0;
        for ($i = 7; $i < $limit; $i++) {

            $result = (1 + ( $i * $m )) % $e;
            // echo "<br>m=".$m;
            // echo "<br>result di d=".$result;
            if ( $result == 0 ) {
                $the_d[] = (1 + ( $i * $m )) / $e;
                // echo "<br>result=".$result;
                // echo "<br>nilai i=".$i;
                // echo "<br>d=".$the_d[$j];
                $j++;
            }
        }

        $this->d_arr = $the_d; 
        $this->d = $the_d[0];
    }

    // recursive function to calculate the Greatest common divisor from two number
    function gcd($x, $y) {
        return (bcmod($x, $y)) ? $this->gcd($y, bcmod($x, $y)) : $y;
    }

    // getter
    function get_n() {
        return $this->n;
    }

    function get_m() {
        return $this->m;
    }

    function get_p() {
        return $this->p;
    }

    function get_q() {
        return $this->q;
    }
    
    function get_e() {
        return $this->e;
    }
    
    function get_d() {
        return $this->d;
    }

    function get_e_arr() {
        return $this->e_arr;
    }

    function get_d_arr() {
        return $this->d_arr;
    }

    // setter
    function set_p($p) {
        $this->p = $p;
        $this->q = $q;
        $this->n = $p * $q;
        $this->m = ($p - 1) * ($q - 1);
        $this->gen_e($this->m);
        $this->gen_d($this->m, $this->e);
    }

    function set_q($q) {
        $this->q = $q;
        $this->n = $p * $q;
        $this->m = ($p - 1) * ($q - 1);
        $this->gen_e($this->m);
        $this->gen_d($this->m, $this->e);
    }
    
    function set_n($n) {
        $this->n = $n;
    }

    function set_m($m) {
        $this->m = $m;
        $this->gen_e($this->m);
        $this->gen_d($this->m, $this->e);
    }
    
    function set_e($e) {
        $this->e = $e;
        $this->gen_d($this->m, $this->e);
    }
    
    function set_d($d) {
        $this->d = $d;
    }
    
}

?>