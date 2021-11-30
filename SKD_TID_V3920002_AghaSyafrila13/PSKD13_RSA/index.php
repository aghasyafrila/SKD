<?php 
    
    include 'Rsa.php';

    $rsa = new Rsa();

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kelompok 5</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
        crossorigin="anonymous"></script>

</head>

<body>

    <header class="container bg-primary text-white">
        <div class="row">
            <div class="col-12 py-4 text-center">
                <h1 class="display-1">Kelompok 5 TID Praktikum SKD</h1>
                <p class="lead">Program Alogoritma RSA Pada PHP</p>
            </div>
        </div>
    </header>

    <main class="container border">
        <div class="row">
            <div class="col-md-4 py-5">
            <div class="card bg-primary">
                  <h3 class="card-header text-white lead">Masukkan Nilai p, Nilai q, dan Teks</h3>
              <div class="card-body bg-light">
                <div class="card-text">
                
                  <form method="POST">
                    <div class="form-floating mb-3">
                      <input type="number" class="form-control" id="pValue" aria-describedby="pValueHelp" name="p_value" value="<?= isset($_POST['p_value']) ? $_POST['p_value'] : ''; ?>">
                      <label for="pValue">Nilai p</label>
                      <div id="pValueHelp" class="form-text">p harus bilangan prima lebih besar dari 7</div>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="number" class="form-control" id="qValue" aria-describedby="qValueHelp" name="q_value" value="<?= isset($_POST['q_value']) ? $_POST['q_value'] : ''; ?>">
                      <label for="qValue">Nilai q</label>
                      <div id="qValueHelp" class="form-text">q harus bilangan prima lebih besar dari 7 dan berbeda dengan p</div>
                    </div>
                    <div class="form-floating mb-3">
                      <textarea class="form-control" id="textValue" rows="3" aria-describedby="textHelp" name="text_value" placeholder="Teks" style="height: 100px"><?= isset($_POST['text_value']) ? $_POST['text_value'] : ''; ?></textarea>
                      <label for="textValue" class="">Teks</label>
                      <div id="textHelp" class="form-text">Ketik teks yang ingin di enkripsi. Atau chipertext yang ingin di dekripsi. Contoh chipertext: 72,89,45,60</div>
                    </div>
                    <input type="submit" name="encrypt" class="btn btn-danger" value="Enkripsi">
                    <input type="submit" name="decrypt" class="btn btn-primary" value="Dekripsi">
                  </form>
                </div>
              </div>
          </div>
        </div>

        <?php
          if ( ( isset($_POST['encrypt']) || isset($_POST['decrypt']) ) && isset($_POST['p_value']) && isset($_POST['q_value']) && isset($_POST['text_value']) ) {
            $p = $_POST['p_value'];
            $q = $_POST['q_value'];
            $text = $_POST['text_value'];
            
            if ( isset($_POST['decrypt']) && preg_match("/[a-zA-Z]/", $text) ) {
                echo '<script>alert("Isi teks untuk proses dekripsi harus berupa angka desimal yang dipisah dengan spasi/simbol.\nContoh: \'72,89,45,60\' atau \'72 89 45 60\'");</script>';
                exit();
                header('Location:index.php');
            }
            
            if ( $p == $q || $p < 10 || $q < 10 || $rsa->check_prime($p) == false || $rsa->check_prime($q) == false ) {
                echo '<script>alert("Isi p dan q harus berupa bilangan prima dan harus lebih besar dari 7\np dan q tidak boleh sama");</script>';
                exit();
                header('Location:index.php');
            }
            
            
            $rsa->gen_key($p, $q);

        ?>

            <div class="col-md-8 py-5">
            <div class="card bg-primary">
              <div class="card-header bg-primary">
                <h1 class="lead text-white">Hasil </h1>
              </div>
              <div class="card-body bg-light">
                  <div class="mb-3 row">
                    <label for="nilai-p" class="col-sm-1 col-form-label">Nilai p</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-p" value="<?= $rsa->get_p() ?>">
                    </div>
                    <label for="nilai-q" class="col-sm-1 col-form-label">Nilai q</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-q" value="<?= $rsa->get_q() ?>">
                    </div>
                    <label for="nilai-n" class="col-sm-1 col-form-label">Nilai n</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-n" value="<?= $rsa->get_n() ?>">
                    </div>
                  </div>
                  <div class="mb-3 row">
                    <label for="nilai-m" class="col-sm-1 col-form-label">Nilai m</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-m" value="<?= $rsa->get_m() ?>">
                    </div>
                    <label for="nilai-e" class="col-sm-1 col-form-label">Nilai e</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-e" value="<?= $rsa->get_e() ?>">
                    </div>
                    <label for="nilai-d" class="col-sm-1 col-form-label">Nilai d</label>
                    <div class="col-sm-3">
                      <input disabled type="text" class="form-control" id="nilai-d" value="<?= $rsa->get_d() ?>">
                    </div>
                  </div>
                  
                  <?php
                    if ( isset($_POST['encrypt']) ) {
                      $encrypted = $rsa->encrypt($text, $rsa->get_e(), $rsa->get_n());
                      $encrypted_arr = preg_split('/[^a-zA-Z0-9]/', $encrypted);
                    ?>
                    <div class="table-responsive">
                      <table class="table table-bordered">
                          <tr>
                            <td>Plainteks</td>
                            <?php
                              foreach (str_split($text) as $tx) {
                                echo "<td>$tx</td>";
                              }
                            ?>
                          </tr>
                          <tr>
                            <td>Plainteks (DEC)</td>
                            <?php
                              foreach (str_split($text) as $tx) {
                                echo "<td>" . ord($tx) . "</td>";
                              }
                            ?>
                          </tr>
                          <tr>
                            <td>Chiperteks (DEC)</td>
                            <?php
                              foreach ($encrypted_arr as $en) {
                                echo "<td>$en</td>";
                              }
                            ?>
                          </tr>                        
                          <tr>
                            <td>Chiperteks</td>
                            <?php
                              foreach ($encrypted_arr as $en) {
                                echo "<td>" . chr($en) . "</td>";
                              }
                            ?>
                          </tr>
                      </table>
                    </div>
                   <div class="mb-3"> 
                     <label for="chipertextResultValue" class="form-labe;">Chiperteks:</label> 
                    <textarea disabled class="form-control" id="chipertextResultValue" aria-describedby="chipertextResultHelp" name="chipertextResult_value" placeholder="Teks" style="height: 120px"><?= $encrypted ?></textarea>
                   </div>
                   <?php
                    }
                  ?>
                  <?php
                    if ( isset($_POST['decrypt']) ) {
                      $decrypted = $rsa->decrypt($text, $rsa->get_d(), $rsa->get_n());
                      $text_arr = preg_split('/[^a-zA-Z0-9]/', $text);
                  ?>
                  <div class="table-responsive">
                      <table class="table table-bordered">
                        <tr>
                          <td>Chiperteks</td>
                          <?php
                            foreach ($text_arr as $tx) {
                              echo "<td>" . chr($tx) . "</td>";
                            }
                            ?>
                        </tr>
                        <tr>
                          <td>Chiperteks (DEC)</td>
                          <?php
                            foreach ($text_arr as $tx) {
                              echo "<td>$tx</td>";
                            }
                          ?>
                        </tr>
                        <tr>
                          <td>Plainteks (DEC)</td>
                          <?php
                            foreach (str_split($decrypted) as $de) {
                              echo "<td>" . ord($de) . "</td>";
                            }
                          ?>
                        </tr>                        
                        <tr>
                          <td>Plainteks</td>
                          <?php
                            foreach (str_split($decrypted) as $de) {
                              echo "<td>$de</td>";
                            }
                          ?>
                        </tr>
                      </table>
                    </div>
                   <div class="mb-3"> 
                     <label for="plaintextResultValue" class="form-label">Plainteks:</label> 
                    <textarea disabled class="form-control" id="plaintextResultValue" aria-describedby="plaintextResultHelp" name="plaintextResult_value" placeholder="Teks" style="height: 120px"><?= $decrypted ?></textarea>
                   </div>
                  <?php
                    }
                  ?>
                  
              </div>
          </div>
        </div>
          <?php } ?>
        </div>
            </div>
            
        </div>
    </main>

    <footer class="container bg-primary text-white">
        <div class="row">
            <div class="col-12 py-4">
                
            </div>
        </div>
    </footer>

</body>

</html>