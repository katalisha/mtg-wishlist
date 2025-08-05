"""test the scraper class"""

from cards.card import Card
from stores.mtgmate_scraper_helper import MtgMateScraperHelper
from decimal import Decimal


def test_comma():
    card = Card(
        "Bennie Bracks, Zoologist", "NCC", "New Capenna Commander", "86", "Normal"
    )
    helper = MtgMateScraperHelper()
    url = helper.url(card)

    assert url == "https://www.mtgmate.com.au/cards/Bennie_Bracks,_Zoologist/NCC/86"


def test_foil():
    card = Card("Boros Guildgate", "GRN", "Guilds of Ravnica", "243", "Foil")

    helper = MtgMateScraperHelper()
    url = helper.url(card)

    assert url == "https://www.mtgmate.com.au/cards/Boros_Guildgate/GRN/243:foil"


def test_ampersand():
    card = Card(
        "Ishgard, the Holy See // Faith & Grief",
        "FIN",
        "Final Fantasy",
        "283",
        "Normal",
    )
    helper = MtgMateScraperHelper()
    url = helper.url(card)

    assert (
        url
        == "https://www.mtgmate.com.au/cards/Ishgard,_the_Holy_See_//_Faith_%26_Grief/FIN/283"
    )


def test_stock_xpath():
    helper = MtgMateScraperHelper()
    stock = helper.find_stock_level(html)
    assert stock == 1


def test_price_xpath():
    helper = MtgMateScraperHelper()
    price = helper.find_price(html)
    assert price == Decimal("36.00")


html = """
<!DOCTYPE html>
<html>

<head>
	<meta property="og:url" content="https://www.mtgmate.com.au/cards/Bennie_Bracks,_Zoologist/NCC/86" />
	<link href="https://www.mtgmate.com.au/cards/Bennie_Bracks,_Zoologist/NCC/86" rel="canonical" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta property="og:title"
		content="Bennie Bracks, Zoologist · New Capenna Commander [NCC] · MTG Card · Australian Magic: The Gathering Singles · MTG MATE" />
	<meta property="og:description" content="Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature&#39;s color.)
At the beginning of each end step, if you created a token this turn, draw a card." />
	<meta property="og:image"
		content="https://df379stvi8n1.cloudfront.net/assets/images/131b7a24-d71a-5a0e-ab07-cab2d527c917" />
	<meta property="og:image:width" content="488px" />
	<meta property="og:image:height" content="680px" />

	<meta property="description" content="Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature&#39;s color.)
At the beginning of each end step, if you created a token this turn, draw a card." />

	<script>
		window.dataLayer = window.dataLayer || [];
	</script>
	<!-- Google Tag Manager -->
	<script>
		(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
      new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
      j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
      'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-567M2HF');
	</script>
	<!-- End Google Tag Manager -->
	<title>Bennie Bracks, Zoologist · New Capenna Commander [NCC] · MTG Card · Australian Magic: The Gathering Singles ·
		MTG MATE</title>
	<meta name="csrf-param" content="authenticity_token" />
	<meta name="csrf-token"
		content="tzxtju5XBWeARMna8n4xv12TySONPqU9c77QWbZNRCcOs4G1Xt6nrg5eNNfY0wTMZcVs6HEnAKWXB1ryx8gx6g==" />


	<link rel="stylesheet" media="all"
		href="https://df379stvi8n1.cloudfront.net/assets/application-d43a4c82b08013fb0d39ea894480221298fd95f7cc4719bbee87a7202fe6c5a5.css" />
	<script
		src="https://df379stvi8n1.cloudfront.net/assets/application-8307d3970c0865b98f1582a388fc766a0ae7bda3642bb57138b491cbb5d9e8b1.js">
	</script>
	<link href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css" rel="stylesheet"
		type="text/css" />
	<script src="//cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
	<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>

	<link href="//cdn.jsdelivr.net/npm/keyrune@latest/css/keyrune.css" rel="stylesheet" type="text/css" />
	<link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.css" rel="stylesheet" type="text/css" />
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"
		integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">

	<script src="https://df379stvi8n1.cloudfront.net/packs/js/application-e5829788d5e1855523c4.js"></script>
	<meta name="google-site-verification" content="F2oEDXlK6_Ann-wkz065u7v-G1IT5mwUR-5wFVnPuRI" />
</head>

<body>
	<!-- Google Tag Manager (noscript) -->
	<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-567M2HF" height="0" width="0"
			style="display:none;visibility:hidden"></iframe></noscript>
	<!-- End Google Tag Manager (noscript) -->

	<style>
		@media (min-width: 576px) and (max-width: 729px) {
			.collapse.navbar-collapse {
				font-size: 0.7em;
			}

			.react-autosuggest__input {
				width: 110px;
			}
		}

		@media (min-width: 730px) and (max-width: 781px) {
			.collapse.navbar-collapse {
				font-size: 0.9em;
			}

			.react-autosuggest__input {
				width: 140px;
			}
		}
	</style>
	<nav class="navbar sticky-top navbar-expand-sm navbar-dark bg-dark">
		<a class="navbar-brand" href="/">
			<img height="30" src="/logo-dark.png" />
      </a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item active dropdown">
						<a class="nav-link dropdown-toggle" href="/magic_sets" id="navbarDropdown" role="button"
							data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							Shop
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<a class="dropdown-item" href="/magic_sets">Magic Sets</a>
							<a class="dropdown-item" href="/cards/decklist_search">Decklist Search</a>
							<a class="dropdown-item" href="/pages/recently-added">Recently Added</a>
						</div>
					</li>
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
							data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							Staples
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<a class="dropdown-item" href="/staples/commander">Commander</a>
							<a class="dropdown-item" href="/staples/7ph">7PH</a>
							<a class="dropdown-item" href="/staples/standard">Standard</a>
							<a class="dropdown-item" href="/staples/modern">Modern</a>
							<a class="dropdown-item" href="/staples/legacy">Legacy</a>
						</div>
					</li>

					<li class="nav-item">
						<div data-react-class="CartQuantityPill"
							data-react-props="{&quot;channelId&quot;:&quot;cartQuantity&quot;,&quot;initialValue&quot;:0}"
							data-react-cache-id="CartQuantityPill-0"></div>
						<a class="nav-link" href="/cart">Cart </a>
					</li>

					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
							data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							About
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<a class="dropdown-item" href="/pages/faq">FAQ</a>
							<a class="dropdown-item" href="/pages/meet-the-team">Meet the Team</a>
							<a class="dropdown-item" href="/pages/browsing-features">Browsing Features</a>
							<a class="dropdown-item" href="/pages/merge_shipping">Add Cards to an Order</a>
							<a class="dropdown-item" href="/pages/returns-policy">Returns Policy</a>
							<a class="dropdown-item" href="/pages/privacy-policy">Privacy Policy</a>
							<a class="dropdown-item" href="/pages/terms-of-service">Terms of Service</a>
						</div>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="/buylist">Sell Your Cards!</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="/cards/visual_hotlist">Visual Hotlist</a>
					</li>
				</ul>

				<ul class="nav navbar-nav navbar-right">
					<li class="nav-item">
						<a class="nav-link" href="/users/sign_in">Sign In</a>
					</li>
				</ul>

				<div class="d-none d-sm-block">
					<div data-react-class="CardSearch"
						data-react-props="{&quot;autocompleteUrl&quot;:&quot;/api/autocomplete&quot;,&quot;url&quot;:&quot;/cards/search&quot;}"
						data-react-cache-id="CardSearch-0"></div>
				</div>
			</div>
			<style>
				.mobile-search-bar {
					padding: 0.25rem;
				}
			</style>
			<div class="mobile-search-bar d-sm-none w-100">
				<div data-react-class="CardSearch"
					data-react-props="{&quot;url&quot;:&quot;/cards/search&quot;,&quot;autocompleteUrl&quot;:&quot;/api/autocomplete&quot;}"
					data-react-cache-id="CardSearch-0"></div>
			</div>
	</nav>
	<div class="container pt-2">

		<script type="application/ld+json">
			{"@context":"https://schema.org/","@type":"Product","name":"Bennie Bracks, Zoologist · New Capenna Commander [NCC] · MTG Card","image":"https://df379stvi8n1.cloudfront.net/assets/images/131b7a24-d71a-5a0e-ab07-cab2d527c917","description":"Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nAt the beginning of each end step, if you created a token this turn, draw a card.","gtin":"","indentifier_exists":false,"brand":{"name":"Magic: The Gathering"},"sku":"370d0c07-6e13-5f31-9121-4cb14fd108f2","offers":{"@type":"Offer","priceCurrency":"AUD","url":"https://www.mtgmate.com.au/cards/Bennie_Bracks,_Zoologist/NCC/86","availability":"https://schema.org/InStock","price":"36.00"}}
		</script>



		<div class="row d-none d-md-block">
			<div class="col">
				<nav aria-label="breadcrumb">
					<ol class="breadcrumb" vocab="https://schema.org/" typeof="BreadcrumbList">
						<li class="breadcrumb-item">
							<a href="/">Home</a>
						</li>
						<li class="breadcrumb-item" property="itemListElement" typeof="ListItem">
							<a typeof="CategoryCode" property="item" href="/magic_sets">
								<span property="name">Sets</span>
							</a>
							<meta property="position" content="1">
						</li>
						<li class="breadcrumb-item" property="itemListElement" typeof="ListItem">
							<a typeof="CategoryCode" property="item" href="/magic_sets/ncc">
								<span property="name">New Capenna Commander</span>
							</a>
							<meta property="position" content="2">
						</li>
						<li class="breadcrumb-item">
							<span>Bennie Bracks, Zoologist</span>
						</li>
					</ol>
				</nav>
			</div>
		</div>

		<div class="row">
			<div class="col">
				<div class="card-info-grid">
					<div class="card-image">
						<div class="" style="border-radius: 5%/4%;">
							<img class="img-fluid" src="https://df379stvi8n1.cloudfront.net/assets/images/131b7a24-d71a-5a0e-ab07-cab2d527c917" style="border-radius: 5%/4%;" />
          </div>
						</div>
						<div class="card-text">
							<h1>
								<strong>
              <a href="/cards/Bennie%20Bracks,%20Zoologist">Bennie Bracks, Zoologist</a>
            </strong>
								</br>
								<span><i class="ms ms-cost ms-3 ms-shadow"></i><i class="ms ms-cost ms-w ms-shadow"></i></span>
							</h1>
							</br>
							<h3>
								<i class="set-code ss ss-ncc ss-mythic" value="ncc"></i>

								<em>
            ·
              <a href="/magic_sets/ncc">New Capenna Commander</a>
            </em>
								<em class="text-muted">
                 · Nonfoil
              </em>
							</h3>
							<p>
								Convoke (Your creatures can help cast this spell. Each creature you tap while casting
								this spell pays for {1} or one mana of that creature&#39;s color.)
								At the beginning of each end step, if you created a token this turn, draw a card.
							</p>
							<p>
								<em>
            His enthusiastic curiosity puts even the most fearsome of beasts at ease.
          </em>
							</p>
						</div>
						<div class="shopping-cart">
							<table class="table table-sm">
								<thead class="thead-light">
									<tr>
										<th class="table-secondary">Current Price</th>
										<th class="table-secondary">In Stock</th>
										<th class="table-secondary">Add to Cart</th>
									</tr>
								</thead>
								<tbody>
									<tr class="magic-card">
										<td class="price">
											$36.00
										</td>
										<td class="available-quantity">
											1
										</td>
										<td class="form">
											<form class="form-inline" action="/cart/add_item" accept-charset="UTF-8"
												method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Vq/SrR4vzNnqLaQwghAFXOlD24lnxyoBuOZprs1VZKpa1Ax3FFwPgS/1rcB5E9c593+ouXDxDj+CDHKNVgBsQA==" />
												<input type="hidden" name="card_sku[id]" value=370d0c07-6e13-5f31-9121-4cb14fd108f2 />
												<input
      class="buy_quantity form-control form-control-sm mb-2 mr-sm-2 col-4"
      name="card_sku[quantity]"
      type="number"
      value="1"
      min="1"
      max="1"
    />
												<button class="btn btn-dark mb-2" type="submit" value="Add to Cart">
     <i class="fa fa-shopping-cart"></i>
  </button>
											</form>
										</td>
									</tr>
								</tbody>
							</table>
							<ul class="list-group" , style="padding-bottom:10px;">
								<li class="list-group-item list-group-item-secondary">Also Printed in:</li>
								<li class="list-group-item">
									<i class="set-code ss ss-ncc ss-mythic" value="ncc"></i>

									<a href="/cards/Bennie_Bracks,_Zoologist/NCC/86:foil">New Capenna Commander</a>
									·
									<span style="background-image:
    linear-gradient(135deg, rgba(222,197,37,0) 0%, rgba(222,197,37,0) 1%, rgba(255,8,8,0.06) 19%, rgba(239,111,23,0.1) 32%, rgba(222,213,37,0.23) 45%, rgba(36,222,101,0.39) 62%, rgba(47,221,109,0.4) 63%, rgba(216,208,239,0.39) 79%, rgba(131,123,173,0.38) 88%, rgba(136,129,178,0.38) 89%, rgba(193,191,234,0) 100%);"
  class="badge badge-label finish">
    Foil
  </span>


									- $43.00
									- <strong>0 in stock</strong>
								</li>
								<li class="list-group-item">
									<i class="set-code ss ss-ncc ss-mythic" value="ncc"></i>

									<a href="/cards/Bennie_Bracks,_Zoologist/NCC/94">New Capenna Commander</a>
									- $37.00
									- <strong>0 in stock</strong>
								</li>
								<li class="list-group-item">
									<i class="set-code ss ss-ncc ss-mythic" value="ncc"></i>

									<a href="/cards/Bennie_Bracks,_Zoologist/NCC/94:foil">New Capenna Commander</a>
									·
									<span style="background-image:
    linear-gradient(135deg, rgba(222,197,37,0) 0%, rgba(222,197,37,0) 1%, rgba(255,8,8,0.06) 19%, rgba(239,111,23,0.1) 32%, rgba(222,213,37,0.23) 45%, rgba(36,222,101,0.39) 62%, rgba(47,221,109,0.4) 63%, rgba(216,208,239,0.39) 79%, rgba(131,123,173,0.38) 88%, rgba(136,129,178,0.38) 89%, rgba(193,191,234,0) 100%);"
  class="badge badge-label finish">
    Foil
  </span>


									- $48.00
									- <strong>0 in stock</strong>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>

			<hr />

			<div class="row">
				<div class="col">
					<div class="text-center">
						Customers who purchased this also bought:
					</div>
				</div>
			</div>

			<div class="row">
				<div class="col">
					<div class="text-center">
						<a class="text-muted" href="/cards/Halo_Fountain/SNC/15">
							<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/280ca4e1-a4c2-5572-963a-d9865265845d" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
							<a class="text-muted" href="/cards/Bootleggers&#39;_Stash/SNC/134">
								<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/da8106d8-e3f3-59e7-9d10-3461ce397b66" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
								<a class="text-muted" href="/cards/Mosswort_Bridge/NCC/415">
									<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/2aa9a10e-51e4-5976-96b4-d71fc6ddf0a0" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
									<a class="text-muted" href="/cards/Fellwar_Stone/NCC/367">
										<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/ac6f8c7f-4046-5c8e-bf21-09fbfca62a93" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
										<a class="text-muted" href="/cards/Arcane_Signet/C21/234">
											<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/955defdb-4baa-54b5-9970-f8485ce30022" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
											<a class="text-muted" href="/cards/Pest_Infestation/C21/65">
												<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/52207051-a7c8-5dd2-b5e5-251d6f5dd3d8" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
												<a class="text-muted" href="/cards/Kari_Zev,_Skyship_Raider/AER/87">
													<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/ddd72d7a-9dc5-537d-87eb-ce440455bfb4" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
													<a class="text-muted" href="/cards/Welcoming_Vampire/VOW/46">
														<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/8db676bc-de61-5485-aaa0-0481de4ee4bd" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
														<a class="text-muted" href="/cards/Human_Soldier/TIKO/5">
															<img height="136" alt="" src="https://df379stvi8n1.cloudfront.net/assets/images/c6a92ac0-5167-5454-8cf9-f9cc8236835e" style="padding-bottom: 5px;
              border-top-left-radius: 5% 4%;
              border-top-right-radius: 5% 4%;
              border-bottom-left-radius: 6% 8%;
              border-bottom-right-radius: 6% 8%;
              ">
            </a>
					</div>
				</div>
			</div>


			<footer class="pt-4 my-md-5 pt-md-5 border-top">
				<div class="row">
					<div class="col-12 col-md">
						<img class="mb-2" src="/logo-light.png" alt="" height="24">
						<small class="d-block mb-3 text-muted">ABN: 11 659 944 199</small>
					</div>
					<div class="col-6 col-md">
						<h5>
							<a class="text-muted" href="/magic_sets">Shop</a>
						</h5>
						<ul class="list-unstyled text-small">
							<li><a class="text-muted" href="/cart">Cart</a></li>
							<li><a class="text-muted" href="/magic_sets">Magic Sets</a></li>
							<li><a class="text-muted" href="/cards/decklist_search">Decklist Search</a></li>
							<li><a class="text-muted" href="/pages/recently-added">Recently Added</a></li>
						</ul>
					</div>
					<div class="col-6 col-md">
						<h5>
							<a class="text-muted" href="/pages/faq">About</a>
						</h5>
						<ul class="list-unstyled text-small">
							<li><a class="text-muted" href="/pages/meet-the-team">Meet the Team</a></li>
							<li><a class="text-muted" href="/pages/browsing-features">Browsing Features</a></li>
							<li><a class="text-muted" href="/pages/merge_shipping">Add Cards to an Order</a></li>
							<li><a class="text-muted" href="/pages/returns-policy">Returns Policy</a></li>
							<li><a class="text-muted" href="/pages/privacy-policy">Privacy Policy</a></li>
							<li><a class="text-muted" href="/pages/terms-of-service">Terms of Service</a></li>
						</ul>
					</div>
				</div>
			</footer>
		</div>
</body>

</html>
"""
