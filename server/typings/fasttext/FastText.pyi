from typing import Any, Literal

from numpy import float32
from numpy.typing import NDArray

type LanguageLabels = Literal[
    '__label__ace_Arab',
    '__label__ace_Latn',
    '__label__acm_Arab',
    '__label__acq_Arab',
    '__label__aeb_Arab',
    '__label__afr_Latn',
    '__label__ajp_Arab',
    '__label__aka_Latn',
    '__label__amh_Ethi',
    '__label__apc_Arab',
    '__label__arb_Arab',
    '__label__arb_Latn',
    '__label__ars_Arab',
    '__label__ary_Arab',
    '__label__arz_Arab',
    '__label__asm_Beng',
    '__label__ast_Latn',
    '__label__awa_Deva',
    '__label__ayr_Latn',
    '__label__azb_Arab',
    '__label__azj_Latn',
    '__label__bak_Cyrl',
    '__label__bam_Latn',
    '__label__ban_Latn',
    '__label__bel_Cyrl',
    '__label__bem_Latn',
    '__label__ben_Beng',
    '__label__bho_Deva',
    '__label__bjn_Arab',
    '__label__bjn_Latn',
    '__label__bod_Tibt',
    '__label__bos_Latn',
    '__label__bug_Latn',
    '__label__bul_Cyrl',
    '__label__cat_Latn',
    '__label__ceb_Latn',
    '__label__ces_Latn',
    '__label__cjk_Latn',
    '__label__ckb_Arab',
    '__label__crh_Latn',
    '__label__cym_Latn',
    '__label__dan_Latn',
    '__label__deu_Latn',
    '__label__dik_Latn',
    '__label__dyu_Latn',
    '__label__dzo_Tibt',
    '__label__ell_Grek',
    '__label__eng_Latn',
    '__label__epo_Latn',
    '__label__est_Latn',
    '__label__eus_Latn',
    '__label__ewe_Latn',
    '__label__fao_Latn',
    '__label__fij_Latn',
    '__label__fin_Latn',
    '__label__fon_Latn',
    '__label__fra_Latn',
    '__label__fur_Latn',
    '__label__fuv_Latn',
    '__label__gla_Latn',
    '__label__gle_Latn',
    '__label__glg_Latn',
    '__label__grn_Latn',
    '__label__guj_Gujr',
    '__label__hat_Latn',
    '__label__hau_Latn',
    '__label__heb_Hebr',
    '__label__hin_Deva',
    '__label__hne_Deva',
    '__label__hrv_Latn',
    '__label__hun_Latn',
    '__label__hye_Armn',
    '__label__ibo_Latn',
    '__label__ilo_Latn',
    '__label__ind_Latn',
    '__label__isl_Latn',
    '__label__ita_Latn',
    '__label__jav_Latn',
    '__label__jpn_Jpan',
    '__label__kab_Latn',
    '__label__kac_Latn',
    '__label__kam_Latn',
    '__label__kan_Knda',
    '__label__kas_Arab',
    '__label__kas_Deva',
    '__label__kat_Geor',
    '__label__knc_Arab',
    '__label__knc_Latn',
    '__label__kaz_Cyrl',
    '__label__kbp_Latn',
    '__label__kea_Latn',
    '__label__khm_Khmr',
    '__label__kik_Latn',
    '__label__kin_Latn',
    '__label__kir_Cyrl',
    '__label__kmb_Latn',
    '__label__kmr_Latn',
    '__label__kon_Latn',
    '__label__kor_Hang',
    '__label__lao_Laoo',
    '__label__lij_Latn',
    '__label__lim_Latn',
    '__label__lin_Latn',
    '__label__lit_Latn',
    '__label__lmo_Latn',
    '__label__ltg_Latn',
    '__label__ltz_Latn',
    '__label__lua_Latn',
    '__label__lug_Latn',
    '__label__luo_Latn',
    '__label__lus_Latn',
    '__label__lvs_Latn',
    '__label__mag_Deva',
    '__label__mai_Deva',
    '__label__mal_Mlym',
    '__label__mar_Deva',
    '__label__min_Arab',
    '__label__min_Latn',
    '__label__mkd_Cyrl',
    '__label__plt_Latn',
    '__label__mlt_Latn',
    '__label__mni_Beng',
    '__label__khk_Cyrl',
    '__label__mos_Latn',
    '__label__mri_Latn',
    '__label__mya_Mymr',
    '__label__nld_Latn',
    '__label__nno_Latn',
    '__label__nob_Latn',
    '__label__npi_Deva',
    '__label__nso_Latn',
    '__label__nus_Latn',
    '__label__nya_Latn',
    '__label__oci_Latn',
    '__label__gaz_Latn',
    '__label__ory_Orya',
    '__label__pag_Latn',
    '__label__pan_Guru',
    '__label__pap_Latn',
    '__label__pes_Arab',
    '__label__pol_Latn',
    '__label__por_Latn',
    '__label__prs_Arab',
    '__label__pbt_Arab',
    '__label__quy_Latn',
    '__label__ron_Latn',
    '__label__run_Latn',
    '__label__rus_Cyrl',
    '__label__sag_Latn',
    '__label__san_Deva',
    '__label__sat_Olck',
    '__label__scn_Latn',
    '__label__shn_Mymr',
    '__label__sin_Sinh',
    '__label__slk_Latn',
    '__label__slv_Latn',
    '__label__smo_Latn',
    '__label__sna_Latn',
    '__label__snd_Arab',
    '__label__som_Latn',
    '__label__sot_Latn',
    '__label__spa_Latn',
    '__label__als_Latn',
    '__label__srd_Latn',
    '__label__srp_Cyrl',
    '__label__ssw_Latn',
    '__label__sun_Latn',
    '__label__swe_Latn',
    '__label__swh_Latn',
    '__label__szl_Latn',
    '__label__tam_Taml',
    '__label__tat_Cyrl',
    '__label__tel_Telu',
    '__label__tgk_Cyrl',
    '__label__tgl_Latn',
    '__label__tha_Thai',
    '__label__tir_Ethi',
    '__label__taq_Latn',
    '__label__taq_Tfng',
    '__label__tpi_Latn',
    '__label__tsn_Latn',
    '__label__tso_Latn',
    '__label__tuk_Latn',
    '__label__tum_Latn',
    '__label__tur_Latn',
    '__label__twi_Latn',
    '__label__tzm_Tfng',
    '__label__uig_Arab',
    '__label__ukr_Cyrl',
    '__label__umb_Latn',
    '__label__urd_Arab',
    '__label__uzn_Latn',
    '__label__vec_Latn',
    '__label__vie_Latn',
    '__label__war_Latn',
    '__label__wol_Latn',
    '__label__xho_Latn',
    '__label__ydd_Hebr',
    '__label__yor_Latn',
    '__label__yue_Hant',
    '__label__zho_Hans',
    '__label__zho_Hant',
    '__label__zsm_Latn',
    '__label__zul_Latn',
]

class _FastText:
    def __init__(self, model_path: str | None = None, args: dict[str, Any] | None = None): ...
    def predict(
        self,
        text: str | list[str],
        k: int = 1,
        threshold: float = 0.0,
        on_unicode_error: str = 'strict',
    ) -> tuple[tuple[LanguageLabels, ...], NDArray[float32]]: ...

def load_model(path: str) -> _FastText: ...
